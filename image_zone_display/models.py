from django.db import models
import jieba
# Create your models here.


#图片类
class Image(models.Model):
    image_title=models.CharField(max_length=20)
    image_url=models.CharField(max_length=100)
    image_description=models.TextField(max_length=200)
    def __str__(self):
        return "%d" % self.pk

    #本类的CRUD操作

    #插入
    def insert_image(self,title,url,description):
        self.image_url = url
        self.image_title = title
        self.image_description = description
        self.save()

        return "insert_success"


    #修改
    #id不为空，某个参数为空时，则这个参数的值不变
    def update_image_by_id(self,id,title,url,description):
        if (id == None and id == ""):
            return False
        image_item=Image.objects.get(id=id)
        if(title!="" and title!=" " and title!=None):
            image_item.image_title=title
        if (url != "" and url != " " and url != None):
            image_item.image_url = url
        if (description != "" and description != " " and description != None):
            image_item.image_description = description
        image_item.save()
        return True

    #删除
    def delete_image(self, id):
        if (id == None and id == ""):
            return False
        image_item=Image.objects.get(id=id)
        image_item.delete()
        return True
