from rest_framework import serializers
from .models import Domain
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import hashlib


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("title", "url", "change")
        model = Domain
        read_only_fields = ("title", "change")

    def make_md5(self, page):
        if type(page) != bytes:
            page = page.encode("utf-8")
        md5 = hashlib.md5(page).hexdigest()
        return md5

    def get_title(self, page):
        soup = BeautifulSoup(page, "html.parser")
        content = soup.find("title").text
        return content

    def append_data(self, url):
        try:
            request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
            response = urlopen(request)
            page = response.read()
            return self.get_title(page), self.make_md5(page)
        except Exception as e:
            print(e)
            return "페이지 에러", ""

    def create(self, validated_data):
        token = self.context.get("token")
        url = validated_data.get("url")
        title, md5 = self.append_data(url)

        print(url, title, md5)
        domain = Domain.objects.create(
            **validated_data, token=token, title=title, html=md5
        )
        return domain
