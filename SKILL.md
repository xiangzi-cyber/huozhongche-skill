---
name: huozhongche-tweet-writing
description: A specialized skill for writing "AI火种车" series tweets. It provides a structured 6-step workflow, from material analysis to final draft, including detailed image selection strategies. Use this for all tweet writing tasks related to the "AI火种车" project.
---

# 火种车推文写作 Skill (V4.5)

This skill provides a structured, six-step workflow for creating high-quality tweets for the "AI火种车" project. It incorporates best practices learned from analyzing previously published articles.

## 核心写作流程

Follow these six steps sequentially. Do not skip steps.

### **步骤一：信息梳理与缺口识别**

1.  **梳理素材**: Read the provided material table (`.xlsx` file).
2.  **判断场域类型**: Categorize the school/event (e.g., "关爱留守儿童", "职业技能提升", "升学导向").
3.  **结构化素材库**: Organize key information into categories:
    *   学校与场域背景
    *   教师相关亮点 (including quotes)
    *   学生活动与小插曲 (including quotes)
    *   现场花絮/彩蛋
4.  **识别信息缺口**: Identify and list critical missing information. The following are **mandatory** items to check:
    *   活动具体日期（年份、月份、日期）
    *   **活动课表**（课表是基础信息，必须主动索取，如未提供需明确提示用户补充）
    *   其他缺失的关键信息（如具体人名等）

### **步骤二：故事挖掘与主线提炼**

1.  Based on the structured material, propose 2-3 potential story angles (e.g., focusing on a student's breakthrough, a teacher's transformation, or a specific event's impact).
2.  Ask the user to choose a primary storyline and, if applicable, a secondary storyline.

### **步骤三：结构与风格选择**

1.  **叙事结构**: Ask the user to choose between:
    *   **A. 线性叙事 (Linear Narrative)**: Best for a single, emotional story.
    *   **B. 模块化报道 (Modular Reporting)**: Best for in-depth reports with large amounts of information. Can embed linear narratives within modules.
2.  **标题风格**: Propose 3 title options based on the chosen storyline:
    *   **A. 新闻风格 (News Style)**
    *   **B. 故事风格 (Storytelling Style)**
    *   **C. 系列报道风格 (Series Style)**

### **步骤四：初稿撰写与主线深化**

1.  Write the first draft based on the selected storyline, structure, and title style.
2.  Apply the following **core writing principles**:
    *   **隐喻贯穿全文**: Find a central metaphor or image that connects the opening, body, and closing (e.g., "折叠的梦想", "补白"). Use it consistently throughout the article to create structural cohesion.
    *   **细节当主角**: Let the most powerful details from the material (a specific quote, a physical object, a child's action) become the emotional core of each module, not just decoration.
    *   **辅助线索克制**: Secondary storylines should support, not compete with, the main theme. Use them sparingly—typically one module—to add texture.
    *   **结尾意象串联**: The closing paragraph should re-weave the most specific and vivid images from each module, letting readers feel the impact rather than stating a conclusion directly.
    *   **词语翻转解读**: When a quote contains a word with a common negative connotation (e.g., "天花乱坠"), consider re-interpreting it positively in context to create an emotional turning point.
    *   **平视视角（核心原则）**: The article must adopt a perspective of **equal respect**, not pity or condescension. The reader should feel "these children are remarkable" rather than "these children are unfortunate." Apply the following rules:
        *   **禁用表达（会引发俧视感）**: 这里的孩子很可怜 / 这里的孩子需要帮助 / 山里的孩子从没见过 / 这里条件有限 / 山区孩子相比城市孩子 / 希望帮助这里的孩子
        *   **推荐替换方向**: 展现孩子们本身的力量、见识和视野（如"他们的世界，从来不小"）；强调孩子们的主动性和创造力；用孩子的原话和行动说话，而不是用大人的视角去评价他们。
        *   **正向叙事角度**: 我们是来记录的，不是来帮助的；火种车是带来资源的，不是带来同情的。
    *   **名言引用规范**: When incorporating quotes from notable figures, follow these rules:
        *   **多元搭配**: Use quotes from at least two different people to avoid monotony. A recommended pattern is: **Opening** (a Chinese leader or policy-level figure for macro authority) + **Closing** (a domestic or international educator for emotional resonance).
        *   **在地相关**: Quotes must be directly relevant to the local geography, history, or cultural background of the school. Avoid generic educational platitudes.
        *   **避免扶贫标签**: Do not use quotes that link education with poverty alleviation (e.g., "扶贫必扶智"), as this creates an unwanted "pity" narrative. Prioritize quotes about technology, dreams, creativity, and the future.
        *   **推荐教育家**: Domestic: 陶行知 (e.g., "把儿童的创造力解放出来"). International: 蒙台梭利, 雅斯贝尔斯 (e.g., "一个灵魂唤醒另一个灵魂").
3.  Perform a self-diagnosis to identify areas for improvement. **Do not show the self-diagnosis in the article output.** Briefly summarize the improvements made in the user-facing message (2-4 bullet points).

### **步骤五：配图策略与建议**

1.  Integrate image suggestions directly into the revised draft using blockquotes.
2.  The suggestions must follow the **Privacy Protection Rules** and the **16 Invisible Requirements for Image Selection** outlined in the section below.
3.  Present the draft with embedded image suggestions to the user for review.

### **步骤六：表达去重与终稿交付 (V2.0 自动化流程)**

**查重目的：** 检查新稿与已发布稿件在**表达层面**的重复，包括相似句式、高频词汇和核心意象，确保系列文章每篇都有独特的语言风格。

**自动化查重流程：**

**1. 准备工作：获取并转换原文**

*   **确认来源**：按以下优先级获取已发布稿件内容：

    | 方式 | 说明 | 可用性 |
    |------|------|--------|
    | **方式一：文件上传** | 用户提供 Word/PDF 文件，直接读取比对 | ✅ 推荐，最稳定 |
    | **方式二：微信链接抓取** | 用户提供微信公众号链接，使用 PC 微信客户端 UA 抓取 | ✅ **可用**，需伪装UA（见下方命令） |
    | **无内容可供比对** | 跳过查重，直接润色终稿 | — |

    **方式二的抓取命令（伪装PC微信客户端UA）：**
    ```bash
    curl -s -L \
      -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555' \
      -H 'Referer: https://mp.weixin.qq.com/' \
      '[微信文章链接]' | python3.11 -c "
import sys
from bs4 import BeautifulSoup
html = sys.stdin.read()
soup = BeautifulSoup(html, 'html.parser')
content = soup.find(id='js_content')
if content:
    print(content.get_text(separator='\\n', strip=True))
"
    ```
    > **注意**：普通浏览器UA、手机微信UA均会被微信服务器端IP检测拦截。只有 `WindowsWechat/WMPF` 这个 PC 微信客户端的 UA 经过验证可以绕过验证。沙盒环境的浏览器工具（browser_navigate）无法访问微信文章，必须用 curl 命令行方式。
*   **创建目录**：为处理文件，创建工作目录。
    ```bash
    mkdir -p /home/ubuntu/published_articles
    ```
*   **文件转换**：将用户提供的所有 PDF 稿件转换为纯文本 `.txt` 文件，并存放到上述目录。对每个文件执行：
    ```bash
    # 将 source.pdf 转换为 target.txt
    pdftotext /path/to/source.pdf /home/ubuntu/published_articles/target.txt
    ```
    *注意：文件名应能区分不同稿件，例如 `站1.txt`, `站2.txt`。*

**2. 执行查重：运行分析脚本**

*   使用技能内置的 `dedup_check.py` 脚本进行自动化分析。该脚本会生成一份包含句子级重复、意象词重叠和高频词分析的综合报告。
*   **执行命令**：
    ```bash
    python3.11 /home/ubuntu/skills/huozhongche-tweet-writing/scripts/dedup_check.py --draft [新稿路径] --published-dir /home/ubuntu/published_articles/
    ```
    *将 `[新稿路径]` 替换为当前待查重稿件的实际路径，例如 `/home/ubuntu/final_case_x.md`。*

**3. 分析报告并提出建议**

*   **解读报告**：仔细阅读脚本输出的报告，重点关注【一】句子级重复、【二】核心意象词汇重叠、【三】高频词汇重叠三个部分。
*   **形成建议**：
    *   对于**句子级重复**，判断是否来自同一稿件的迭代（可忽略）或跨稿件的重复（需修改）。
    *   对于**意象词和高频词**，重点关注在已发布稿件中出现次数过多（如超过10次）且在新稿中再次出现的词汇。
    *   将需要修改的词汇和具体上下文整理成表格，向用户提出具体的替换建议。

**4. 错别字检查**

在交付终稿前，必须对稿件进行一次错别字检查。中文错别字工具无法自动检测，需由 AI 逐句阅读稿件全文，重点检查以下常见类型：

*   **形近字混淆**：如“己”与“巳”、“己”与“已”、“机器狗”与“机器狗”、“搞档”与“搞档”等。
*   **同音字误用**：如“辭代”应为“迭代”、“机场”应为“机场”等。
*   **漏字/多字**：句子是否完整、标点符号是否正确。
*   **人名/地名拼写一致性**：确认全文中所有人名、地名的写法前后一致（如“磐子崂”与“磐子崂”不应混用）。

将发现的所有错误整理成表格（行号、原文、建议修正），向用户确认后执行修正。

**5. 修改并交付终稿**

*   **执行修改**：根据用户确认的建议，使用 `file` 工具的 `edit` 功能对稿件进行精准替换。
*   **最终交付**：向用户交付修改后的最终稿（`.md` 文件），并附上修改前后的对比说明，完成校验流程。

---

## 文件结构规范

稿件 `.md` 文件内部的标题层级需遵循以下规范：

- **主标题**：不写入 `.md` 文件，在发布时作为文章标题使用。
- **一级标题 (`#`)**：用于文章内部大的章节或日期分隔，如 `# Day 1: 六城奔赴，一夜星光`。
- **二级标题 (`##`)**：用于段落的小标题，如 `## 教师组`。标题与正文内容必须分行，不可将正文连在标题后。

---

## 系列推文写作经验

以下是在实际写作中沉淀的确定性经验，适用于所有火种车推文。

**标题风格延续性**：系列文章的标题应保持一致的格式风格。已确认的模式为“事件节点：一句话总结”，如《出发倒计1天：这一次，AI火种车驶向陇南》、《志愿者集结日：AI 火种车，六城星光汇于一处》。每篇新标题应主动对齐已发布的标题风格。

**结尾视角选择**：推文结尾应采用“见证者”视角，而非“参与者”视角。避免“我们在XX等你”这种强行拉读者入戏的表达，改用“欢迎你和我们一起，成为这个故事的见证者”等自然的邀请式结尾。

**不确定信息处理**：对于时间、地点、人名等关键信息尚不确定的，一律隐藏不写，待确认后再补充，不可猜测。

**鸣谢语必须包含的内容**：每篇推文必须在文末加入对华为TECH4ALL数字包容与西部阳光基金会的鸣谢语。参考语句：“特别鸣谢华为TECH4ALL数字包容与西部阳光基金会对本项目的公益支持，让科技的温度得以翻山越岭。”

**志愿者推文的人物细节原则**：写志愿者集结、备战等团队内部推文时，必须将具体人物写入正文，包括具体分工、发言金句、现场状态等。避免只写“团队”这个抗象概念，让每个人的名字和行动都出现在文字里。

---

## **配图隐私保护红线 (Privacy Protection Rules) — 最高优先级**

These rules override all other image selection guidelines.

*   **严禁**：学生脸部正面特写照片。
*   **优先**：背影、侧影、低头操作、从背后拍摄的全景——这些既有人物活动感，又保护了学生隐私。
*   **可用**：远景中的人物（面部不清晰）、孩子的手部特写、孩子的作品/笔记特写。
*   **封面图原则**：有人物活动的场景（如操场踢球的远景）比纯风景照更有生活感，但若有人物，须确保面部不清晰或为背影/侧影。

---

## **配图的16条隐形要求 (The 16 Invisible Requirements for Image Selection)**

These are mandatory guidelines for Step 5. Apply after ensuring Privacy Protection Rules are met.

1.  **开篇要宏大 (Grandiose Opening)**: Use a wide-angle shot combining the school environment with human activity (e.g., children playing on the field with mountains in the background) to establish context. Avoid pure landscape shots with no people.
2.  **身份须明确 (Clear Identity)**: Must include a clear shot of the school gate or nameplate (full gate view preferred over close-up) as an identity marker.
3.  **概念图形化 (Visualize Concepts)**: For abstract or complex concepts/models (e.g., "1133+n"), prioritize using an infographic over a photo.
4.  **特写显细节 (Details in Close-ups)**: Use close-ups effectively (on name tags, hands, stationery, screen details, carved text on desks) to focus on the subject and add narrative depth.
5.  **作品即成果 (Showcase the Work)**: Outputs from students or teachers (drawings, notes, code, AI-generated PPT on phone screen) are excellent visual materials and should be actively suggested.
6.  **界面即内容 (Interface is Content)**: When mentioning specific software, tools, or online works, showing a direct screenshot is the most intuitive method.
7.  **反馈即价值 (Feedback is Value)**: Capture moments that signify "value" and "positive feedback," such as applause, taking photos with phones, or raising hands. These are more powerful than static shots of an audience listening.
8.  **协作显社群 (Collaboration Shows Community)**: Suggest scenes of "collaborative learning," like group discussions, people looking at the same screen, or sharing results, to convey a sense of community.
9.  **合影显成功 (Group Photos Signify Success)**: The final image should ideally be a group photo with students and teachers (holding certificates if available). This conveys a sense of achievement and ends the article on a positive, uplifting note.
10. **情绪抓人心 (Emotion is Engaging)**: Prioritize photos that clearly capture the positive emotions of participants. For children, use action shots (peeking through a door, looking up at a screen) rather than posed portraits.
11. **讲师须在场 (The Speaker Must Be Present)**: Must include at least one photo of the lecturer or speaker giving their presentation, including preparation shots (e.g., setting up equipment).
12. **拼图讲故事 (Tell Stories with Collages)**: Suggest using collages or side-by-side comparisons to juxtapose a tool/product with the human reaction to it, creating a cause-and-effect narrative.
13. **动作代替面孔 (Action Over Faces)**: Capture action-driven moments (children peeking through a door crack, backs of children looking at a blackboard) rather than direct face shots. These are more narrative and privacy-safe.
14. **实物优于截图 (Physical Objects Over Screenshots)**: When possible, suggest using a photo of a physical object (e.g., a child holding a printed AI-generated character) instead of a screen screenshot. Physical objects carry more warmth and authenticity.
15. **黑板即叙事 (Blackboard as Narrative)**: Blackboards with student-written text (e.g., "我们的新朋友——AI火种车") or chalk drawings are powerful narrative devices. Actively suggest them when mentioned in the material.
16. **准备即付出 (Preparation Shows Effort)**: Include at least one "behind-the-scenes" or preparation photo (e.g., teachers setting up equipment late at night) to convey the effort invested by the team.



---

## 语言风格润色规范 (Language Style Polishing Guidelines)

以下是从优秀润色稿中提炼的语言风格规范，用于提升文案的正式感和精炼度。

| 类别 | 倾向规避的表达 | 推荐使用的风格 | 示例 |
|---|---|---|---|
| **动词** | 口语化、直白动词 | 书面语动词，增加正式感 | “出发” → “踏上征程” / “启程” |
| **连接词** | “然后”、“接着”等口语连词 | 省略或用时间/逻辑状语过渡 | “然后她说了这样一句话” → “‘我们在赋能...’这句话...” |
| **形容词** | 普通形容词 | 四字成语、对仗结构 | “很忙” → “各司其职、全力备战” |
| **句子结构** | 简单句堆砌 | 带有修饰成分的长句，增强文采 | “他们从六座城市出发” → “从六座城市出发，穿越大半个中国，向着...同向而行” |
| **情感表达** | 直接抒情 | 场景烘托，意象传递 | “大家都很感动” → “夜色渐浓，备课场地的灯火接续昨夜星光” |
