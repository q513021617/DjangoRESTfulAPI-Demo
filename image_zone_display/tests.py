from django.test import TestCase

# Create your tests here.
from image_zone_display.models import Image
from django.test import TestCase
import logging
#增


logger=logging.getLogger('console')






class ImageTese(TestCase):

    def setUp(self):
        logger.info("=========image测试开始=====")

    def test_add(self):


        title="中国性感高挑美女张馥棋写真图"
        url="http://t2.hddhhn.com/uploads/tu/201702/532/31.jpg"
        description="中国性感高挑美女张馥棋写真图"
        images_item=Image()
        ##count=images_item.objects.count()

        print("=======开始插入记录==========")
        images_item.insert_image(title,url,description)
        # images_item.image_url=url
        # images_item.image_title=title
        # images_item.image_description=description
        # images_item.save()
        print("=======记录增加成功！==========")


        print("=======查询id为1的记录==========")
        item = Image.objects.get(id=1)
        print("title:" + item.image_title)
        print("=======查询成功==========")

        print("=======开始修改记录==========")

        flag=images_item.update_image_by_id(1,"美女张馥棋写真图","","")
        if(flag):
            print("=======修改记录成功==========")

        item = Image.objects.get(id=1)
        print("title:" + item.image_title)

        print("=======开始删除记录==========")
        is_delete=images_item.delete_image(1)
        if(is_delete):
            print("=======删除记录成功==========")

        self.assertEqual(images_item.image_title,"中国性感高挑美女张馥棋写真图")
    def tearDown(self):
        print("==========image测试完成=====")
#删

#改

#查