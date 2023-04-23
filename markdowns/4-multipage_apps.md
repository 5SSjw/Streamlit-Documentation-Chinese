# Multipage apps

随着应用程序变得越来越大，将它们组织成多个页面变得非常有用。这使得开发人员更容易管理应用程序，用户也更容易浏览应用程序。Streamlit提供了一种创建多页面应用的无障碍方式。页面会自动显示在应用程序侧边栏内的一个漂亮的导航小部件中，点击一个页面将导航到页面，而无需重新加载前端——这使得应用程序浏览非常快!

我们在[上一节](https://docs.streamlit.io/library/get-started/create-an-app)中创建了一个“单页应用程序”，探索纽约市的公共优步数据集。在本指南中，让我们学习如何创建多页应用程序。一旦我们对创建多页面应用程序有了坚实的基础，我们就可以在[下一节](https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app)中为自己构建一个!

## 构造多页应用程序

让我们来了解一下创建多页应用程序需要什么——包括如何定义页面，结构化和运行多页应用程序，以及如何在用户界面中在页面之间导航。一旦你理解了基础知识，你就可以直接跳到[下一节](https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app)，将熟悉的`streamlit hello`命令转换为多页面应用程序!

## 运行一个多页应用程序

运行多页应用程序与运行单页应用程序是相同的。运行多页应用程序的命令是:

```
streamlit run [entrypoint file]
```

“入口点文件”是应用程序将显示给用户的第一页。一旦你添加了页面到你的应用程序，入口点文件在侧边栏显示为最顶部的页面。你可以把入口点文件看作应用程序的“主页”。例如，假设您的入口点文件是`Home.py`。然后，要运行你的应用程序，你可以运行`streamlit run Home.py`，这将启动您的应用程序并执行`Home.py`中的代码。

## 添加页面

一旦创建了入口点文件，就可以通过在相对于入口点文件的`pages/`目录中创建`.py`文件来添加页面。例如，如果你的入口点文件是`Home.py`，那么你可以创建一个`pages/About.py`文件来定义“About”页面。下面是一个多页面应用的有效目录结构:

```
Home.py # 这是使用“streamlit run”运行的文件
└─── pages/
  └─── About.py # 这是一个页面
  └─── 2_Page_two.py # 这是另一页
  └─── 3_😎_three.py # 这是第三页
```

> **提示**
> 在文件名中添加表情符号时，最好的做法是包含一个编号前缀，以便在终端中更容易自动补全。终端自动完成可能会被unicode(这是表情符号的表示方式)弄糊涂。

页面被定义为`Pages /`目录下的`.py`文件。页面的文件名根据[下面一节](https://docs.streamlit.io/library/get-started/multipage-apps#how-pages-are-labeled-and-sorted-in-the-ui)中的规则转换为侧边栏中的页面名称。例如，`About.py`文件将在侧边栏中显示为“About”，`2_Page_two.py`显示为“Page two”，`3_😎_three.py`显示为“😎three”

![](4-Multipage apps.assets/Snipaste_2023-04-14_20-02-48.png)

只有`pages/`目录中的`.py`文件才会被加载为页面。Streamlit忽略`pages/`目录和子目录中的所有其他文件。

## 页面在用户界面中是如何被标记和排序的

侧边栏UI中的页面标签是根据文件名生成的，它们可能与[st.set_page_config](https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config)中设置的页面标题不同。让我们了解一下什么构成了页面的有效文件名，页面如何在侧栏中显示，以及页面如何排序。

### 页的有效文件名

文件名由四个不同的部分组成:

1. 一个数字——如果文件前缀是一个数字。
2. 分隔符——可以是`_` ，`-` ，空格或它们的任何组合。
3. 一个标签——它是`.py` 之前的所有内容，但不包括`.py` 。
4. 扩展名——始终是`.py` 。

### 页面如何在侧栏中显示

在侧边栏中显示的是文件名的部分:

- 如果没有标签，Streamlit使用数字作为标签。
- 在UI中，Streamlit通过将`_`替换为空格来美化标签。

### 页面如何在侧栏中排序

排序将文件名中的数字视为实际数字(整数):

- 有数字的文件出现在没有数字的文件之前。
- 文件根据数字(如果有)和标题(如果有)进行排序。
- 当文件排序时，Streamlit将数字视为实际数字而不是字符串。所以03和3是一样的。

此表显示了文件名及其对应标签的示例，按照它们在侧栏中出现的顺序进行排序。

**示例**:

| **文件名**              | **显示标签**     |
| ----------------------- | ---------------- |
| 1 - first page.py       | first page       |
| 12 monkeys.py           | monkeys          |
| 123.py                  | 123              |
| 123_hello_dear_world.py | hello dear world |
| _12 monkeys.py          | 12 monkeys       |

> **提示**
> 表情符号可以让你的网页名称更有趣!例如，一个名为“🏠_Home.py”的文件将在侧栏中创建一个名为“🏠Home”的页面。

## 页面间导航

页面会自动显示在应用程序侧边栏内的一个漂亮的导航UI中。当你在侧边栏UI中单击一个页面时，Streamlit导航到该页面而无需重新加载整个前端——使得应用程序浏览非常快!

您还可以使用url在页面之间导航。页面有自己的url，由文件的标签定义。当多个文件具有相同的标签时，Streamlit会选择第一个([基于上面描述的顺序](https://docs.streamlit.io/library/get-started/multipage-apps#how-pages-are-sorted-in-the-sidebar))。用户可以通过访问页面的URL来查看特定的页面。

如果用户试图访问一个不存在的页面的URL，他们会看到如下所示的模式，说用户请求了一个不在应用程序或目录中的页面。

![](4-Multipage apps.assets/Snipaste_2023-04-14_20-09-42.png)

## 注意事项

- 页面支持[魔术命令](https://docs.streamlit.io/library/api-reference/write-magic/magic)。

- 页面支持run-on-save。此外，当您保存页面时，这将导致当前正在查看该页面的用户重新运行该页面。

- 添加或删除页面会导致UI立即更新。

- 在侧栏中更新页面不会重新运行脚本。

- `st.set_page_config`在页面级别工作。当您使用[st.set_page_config](https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config)设置标题或图标时，这只适用于当前页面。

- 页面全局共享相同的Python模块:

  ```
  # page1.py
  import foo
  foo.hello = 123
  
  # page2.py
  import foo
  # If page1 already executed, this should write 123
  st.write(foo.hello)  
  ```

- 页面共享相同的[st.session_state](https://docs.streamlit.io/library/advanced-features/session-state):

```
# page1.py
import streamlit as st
if "shared" not in st.session_state:
   st.session_state["shared"] = True

# page2.py
import streamlit as st
st.write(st.session_state["shared"])
# If page1 already executed, this should write True
```

现在您已经对多页面应用程序有了很好的理解。您已经学习了如何在用户界面中构建应用程序、定义页面以及在页面之间导航。是时候创建你的第一个[多页面应用程序](https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app)了!🥳