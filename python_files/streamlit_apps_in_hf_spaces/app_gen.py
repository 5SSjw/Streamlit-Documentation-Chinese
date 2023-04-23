# This file is .....
# Author: Hanbin Wang
# Date: 2023/4/18
import transformers
import streamlit as st
from PIL import Image

from transformers import RobertaTokenizer, T5ForConditionalGeneration
from transformers import pipeline

@st.cache_resource
def get_model(model_path):
    tokenizer = RobertaTokenizer.from_pretrained(model_path)
    model = T5ForConditionalGeneration.from_pretrained(model_path)
    model.eval()
    return tokenizer, model


def main():
    # `st.set_page_config` is used to display the default layout width, the title of the app, and the emoticon in the browser tab.

    st.set_page_config(
        layout="centered", page_title="MaMaL-Gen Demo(代码生成)", page_icon="❄️"
    )

    c1, c2 = st.columns([0.32, 2])

    # The snowflake logo will be displayed in the first column, on the left.

    with c1:
        st.image(
            "./panda23.png",
            width=100,
        )

    # The heading will be on the right.

    with c2:
        st.caption("")
        st.title("MaMaL-Gen(代码生成)")


    ############ SIDEBAR CONTENT ############

    st.sidebar.image("./panda23.png",width=270)

    st.sidebar.markdown("---")

    st.sidebar.write(
    """
    ## 使用方法：
    在【输入】文本框输入自然语言，点击【生成】按钮,即会生成想要的代码。
    """
    )

    st.sidebar.write(
    """
    ## 注意事项：
    1）APP托管在外网上，请确保您可以全局科学上网。
    
    2）您可以下载[MaMaL-Gen](https://huggingface.co/hanbin/MaMaL-Gen)模型，本地测试。（无需科学上网）
    """
    )
    # For elements to be displayed in the sidebar, we need to add the sidebar element in the widget.

    # We create a text input field for users to enter their API key.

    # API_KEY = st.sidebar.text_input(
    #     "Enter your HuggingFace API key",
    #     help="Once you created you HuggingFace account, you can get your free API token in your settings page: https://huggingface.co/settings/tokens",
    #     type="password",
    # )
    #
    # # Adding the HuggingFace API inference URL.
    # API_URL = "https://api-inference.huggingface.co/models/valhalla/distilbart-mnli-12-3"
    #
    # # Now, let's create a Python dictionary to store the API headers.
    # headers = {"Authorization": f"Bearer {API_KEY}"}


    st.sidebar.markdown("---")

    st.write(
        "> **Tip：** 首次运行需要加载模型，可能需要一定的时间！"
    )

    st.write(
        "> **Tip：** 左侧栏给出了一些good case 和 bad case，you can try it！"
    )
    st.write(
        "> **Tip：** 不支持中文，输入过长，效果会变差。只支持Python语言"
    )

    st.sidebar.write(
        "> **Good case：**"
    )
    code_good = """1)Convert a SVG string to a QImage
2)Try to seek to given offset"""
    st.sidebar.code(code_good, language='python')

    st.sidebar.write(
        "> **Bad cases：**"
    )
    code_bad = """Read an OpenAPI binary file ."""
    st.sidebar.code(code_bad, language='python')

    # Let's add some info about the app to the sidebar.

    st.sidebar.write(
    """
    App 由 东北大学NLP课小组成员创建， 使用 [Streamlit](https://streamlit.io/)🎈 和 [HuggingFace](https://huggingface.co/inference-api)'s [MaMaL-Gen](https://huggingface.co/hanbin/MaMaL-Gen) 模型.
    """
    )

    # model, tokenizer = load_model("hanbin/MaMaL-Gen")
    st.write("### 输入：")
    input = st.text_area("", height=100)
    button = st.button('生成')

    tokenizer,model = get_model("E:\DenseRetrievalGroup\CodeT5-base-gen")

    input_ids = tokenizer(input, return_tensors="pt").input_ids
    generated_ids = model.generate(input_ids, max_length=100)
    output = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    # generator = pipeline('text-generation', model="E:\DenseRetrievalGroup\CodeT5-base")
    # output = generator(input)
    # code = '''def hello():
    #     print("Hello, Streamlit!")'''
    if button:
        st.write("### 输出：")
        st.code(output, language='python')
    else:
        st.write('####         输出位置~~')





if __name__ == '__main__':

    main()






