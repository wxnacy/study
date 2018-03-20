'''markdown工具类'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseObject
from app.config import BaseConfig
import mistune
import markdown
import markdown2


#  md = mistune.Markdown()
EXT = ['markdown.extensions.extra','markdown.extensions.toc',
        'markdown.extensions.codehilite']
md = markdown.Markdown(extensions=EXT)
#  md = markdown2.Markdown(extras=["code-friendly", "fenced-code-blocks",
    #  "header-ids", "toc"])


class Markdown(BaseObject):
    def __init__(self, *args, **kwargs):
        self.name = (args[0] if args else kwargs.get('name')) or ''

        content = kwargs.get('content')

        if self.name:
            path = '{}{}'.format(BaseConfig.ARTICLE_DIR, self.name)
            with open(path) as f:
                self.content = f.read()

        if content:
            self.content = content

        self.parse_content()

    def parse_content(self):
        self.title = self.content.split('\n')[0][2:]
        #  self.html = md(self.content)
        self.html = md.convert(self.content)
        self.route = '/' + '/'.join(self.name[:-3].split('-', 4))


if __name__ == '__main__':

    #  name = 'test-2017-08-11-basic.md'
    #  md = Markdown(name)
    #  print(md.content)
    #  print(md.title)
    #  print(md.to_dict())
    #  print(md.html)

    content = '# title \n## 你好 ### hao'
    md = Markdown(content=content)
    print(md.html)
