class CodeBlocks:

    def box(text: str, lang: str):
        return "```{}\n{}\n```".format(lang, text)

    def backtick(text: str):
        return "`{}`".format(text)
        