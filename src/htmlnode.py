class HTMLNode:
    def __init__(
            self, tag: str | None = None,
            value: str | None = None,
            children: list["HTMLNode"] | None = None,
            props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Error: to_html method not implemented")

    def props_to_html(self) -> str:
        if self.props != None and self.props:
            return "".join([f" {key}=\"{value}\"" for key, value in self.props.items()])
        return ""

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(
        self, tag: str | None,
        value: str,
        props: dict[str, str] | None = None
    ):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("Error: LeafNode has no value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
