text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"



class TextNode:

        def __init__(self, text, text_type, url=None) -> None:
                self.text = text
                self.text_type = text_type
                self.url = url
        
        def __eq__(self, other) -> bool:
                if self.text == other.text:
                    if self.text_type == other.text_type:
                        if self.url == other.url:
                            return True
        
        def __repr__(self):
              if self.__eq__(self) == True:
                    return f"TextNode({self.text}, {self.text_type}, {self.url})"
                    
