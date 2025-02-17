# Author:           Arturo Aguilar Lagunas
# Pexels Website:   https://www.pexels.com
# class information:
#     Photo's data stucture
class Photo:
    def __init__(self, json_photo):
        self.__photo = json_photo
    @property
    def id(self):
        return int(self.__photo["id"])
    @property
    def width(self):
        return int(self.__photo["width"])
    @property
    def height(self):
        return int(self.__photo["height"])
    @property
    def photographer(self):
        return self.__photo["photographer"]
    @property
    def url(self):
        return self.__photo["url"]
    @property
    def description(self):
        # Make sure alt actually contains text. if it doesn't, which sometimes happens, switch to an alternative method.
        if self.__photo["alt"]:
            return self.__photo["alt"].lower()
        else:
            photo_description_text_in_list_form = self.url.split("/")[-2].replace("-{}".format(self.id), "")
            return ''.join(photo_description_text_in_list_form).replace("-", " ")
    @property
    def color(self):
        return self.photo["avg_color"]
    @property
    def original(self):
        return self.__photo["src"]["original"]
    @property
    def compressed(self):
        return self.original + "?auto=compress"
    @property
    def large2x(self):
        return self.__photo["src"]["large2x"]
    @property
    def large(self):
        return self.__photo["src"]["large"]
    @property
    def medium(self):
        return self.__photo["src"]["medium"]
    @property
    def small(self):
        return self.__photo["src"]["small"]
    @property
    def portrait(self):
        return self.__photo["src"]["portrait"]
    @property
    def landscape(self):
        return self.__photo["src"]["landscape"]
    @property
    def tiny(self):
        return self.__photo["src"]["tiny"]
    @property
    def extension(self):
        return self.original.split(".")[-1]
