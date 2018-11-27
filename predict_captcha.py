# -*- coding:utf-8 -*-
from PIL import Image, ImageFilter
import tensorflow as tf
import numpy as np
import string
import sys
import generate_captcha
import captcha_model
import gen_check_code_test

if __name__ == '__main__':
    captcha = generate_captcha.generateCaptcha()
    width, height, char_num, characters, classes = captcha.get_parameter()
    image_list = gen_check_code_test.get_list()
    # gray_image = Image.open(sys.argv[1]).convert('L')
    x = tf.placeholder(tf.float32, [None, height, width, 1])
    keep_prob = tf.placeholder(tf.float32)

    model = captcha_model.captchaModel(width, height, char_num, classes)
    y_conv = model.create_model(x, keep_prob)
    predict = tf.argmax(tf.reshape(y_conv, [-1, char_num, classes]), 2)
    init_op = tf.global_variables_initializer()
    saver = tf.train.Saver()
    # gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.95)
    # with tf.Session(config=tf.ConfigProto(log_device_placement=False, gpu_options=gpu_options)) as sess:
    with tf.Session() as sess:
        sess.run(init_op)
        saver.restore(sess, "emsModel/crack_capcha.model")
        n = 0
        for i in range(0,len(image_list)):
            realNum, gray_image = gen_check_code_test.gen_captcha_text_and_image_new(i)
            img = np.array(gray_image.getdata())
            test_x = np.reshape(img, [height, width, 1]) / 255.0
            pre_list = sess.run(predict, feed_dict={x: [test_x], keep_prob: 1})
            for i in pre_list:
                s = ''
                for j in i:
                    s += characters[j]
                if realNum.lower() == s.lower():
                    n += 1
                # print("正确: {}  预测: {}".format(realNum, s))
        print(n)