class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):        
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None,  props=None):
        super().__init__(tag, value, props)
        self.tag = tag
        self.value =  value
        self.props = props
        

    def to_html(self):
        if self.tag is None:
           return self.value
        if self.value is None:
           raise ValueError("No value available")
        if self.tag == "p":        
           return f"<{self.tag}>{self.value}</{self.tag}>"

       