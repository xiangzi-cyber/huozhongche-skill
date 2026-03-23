
import re
import os
import argparse
from collections import Counter

# --- Argument Parsing ---
def setup_parser():
    parser = argparse.ArgumentParser(description='Compare a new draft against a directory of published articles for text overlap.')
    parser.add_argument('--draft', type=str, required=True, help='Path to the new draft file (e.g., /home/ubuntu/final_case5.md).')
    parser.add_argument('--published-dir', type=str, required=True, help='Path to the directory containing published articles as .txt files.')
    return parser

# --- File Reading ---
def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Error: File not found at {path}")
        return ""

def load_published_articles(directory):
    articles = {}
    if not os.path.isdir(directory):
        print(f"❌ Error: Directory not found at {directory}")
        return articles
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            name = os.path.splitext(filename)[0]
            articles[name] = read_file(os.path.join(directory, filename))
    return articles

# --- Analysis Functions ---
def extract_sentences(text):
    text = re.sub(r'\s+', '', text)
    sentences = re.split(r'[。！？…!?]', text)
    return [s.strip() for s in sentences if len(s.strip()) >= 10] # Min sentence length

def get_top_words(text, top_n=30):
    text = re.sub(r'[^\u4e00-\u9fff]', '', text)
    words = []
    # Extract 2, 3, and 4-character words
    for i in range(len(text) - 1):
        words.append(text[i:i+2])
    for i in range(len(text) - 2):
        words.append(text[i:i+3])
    for i in range(len(text) - 3):
        words.append(text[i:i+4])
    
    stopwords = {'的', '了', '在', '是', '和', '与', '也', '都', '有', '这', '那', '他', '她', '我', '你', '们', '就', '但', '而', '不', '没', '很', '更', '最', '被', '把', '让', '从', '到', '为', '以', '对', '中', '上', '下', '里', '来', '去', '说', '看', '想', '知', '得', '着', '过', '会', '能', '可', '要', '用', '时', '当', '如', '所', '其', '此', '该', '这个', '那个', '一个', '什么', '怎么', '为什么', '因为', '所以', '虽然', '但是', '如果', '已经', '还是', '或者', '以及', '之后', '之前', '之中', '之间', '建议', '配图', '场景', '构图', '氛围'}
    
    word_freq = Counter(words)
    # Filter out stopwords and single characters
    filtered_words = [(w, c) for w, c in word_freq.most_common(top_n * 3) if not any(sw in w for sw in stopwords) and len(w) >= 2]
    return filtered_words[:top_n]

# --- Main Logic ---
def main():
    parser = setup_parser()
    args = parser.parse_args()

    new_draft = read_file(args.draft)
    published = load_published_articles(args.published_dir)
    
    if not new_draft or not published:
        print("Exiting due to file loading errors.")
        return

    all_published_text = '\n'.join(published.values())

    # 1. Sentence-level check
    print("=" * 60)
    print("【一】句子级重复检测")
    print("=" * 60)
    new_sentences = extract_sentences(new_draft)
    found_duplicates = False
    for sent in new_sentences:
        key = sent[:15] # Use a 15-char key for matching
        for pub_name, pub_text in published.items():
            if key in re.sub(r'\s+', '', pub_text):
                print(f"  ⚠️  [{pub_name}] 发现相似句: {sent[:40]}...")
                found_duplicates = True
                break
    if not found_duplicates:
        print("  ✅ 未发现直接重复的句子。")

    # 2. Imagery word check
    print("\n" + "=" * 60)
    print("【二】核心意象词汇重复检测")
    print("=" * 60)
    imagery_words = ['眼里有光', '闪着光', '被点燃', '点燃', '火种', '星星之火', '打开一扇', '推开一扇', '第一次', '从未见过', '山里的孩子', '大山里', '走出去', '走向世界', '改变命运', '种下', '播下', '跨越', '魔法', '奇迹', '守望', '守护', '边境', '边疆', '补白', '空白', '连接', '桥梁', '希望', '梦想', '未来', '温暖', '温度']
    print(f"{'词汇':<15} {'新稿次数':>10} {'已发布总次数':>15} {'状态':>8}")
    print("-" * 55)
    high_overlap_words = []
    for word in imagery_words:
        new_count = new_draft.count(word)
        pub_count = all_published_text.count(word)
        if new_count > 0 or pub_count > 0:
            status = "⚠️ 高重叠" if (new_count > 0 and pub_count > 10) else ("⚠️ 重叠" if (new_count > 0 and pub_count > 0) else ("🆕 新用" if new_count > 0 else ""))
            if new_count > 0 and pub_count > 0:
                high_overlap_words.append((word, new_count, pub_count))
            print(f"  {word:<13} {new_count:>10} {pub_count:>15}   {status}")

    # 3. High-frequency word check
    print("\n" + "=" * 60)
    print("【三】新稿高频词汇 TOP 20")
    print("=" * 60)
    new_top_words = get_top_words(new_draft)
    pub_freq = Counter(get_top_words(all_published_text, top_n=1000))
    print(f"{'词汇':<12} {'新稿频次':>8} {'已发布频次':>10} {'重叠状态':>10}")
    print("-" * 45)
    for word, count in new_top_words:
        pub_count = pub_freq.get(word, 0)
        overlap = "⚠️ 高重叠" if pub_count > 5 else ("有重叠" if pub_count > 0 else "")
        print(f"  {word:<10} {count:>8} {pub_count:>10}   {overlap}")

    # 4. Summary
    print("\n" + "=" * 60)
    print("【四】查重总结")
    print("=" * 60)
    cn_pattern = re.compile(r'[\u4e00-\u9fff]')
    new_cn_count = len(cn_pattern.findall(new_draft))
    pub_cn_count = len(cn_pattern.findall(all_published_text))
    print(f"新稿字数：约 {new_cn_count} 字 | 已发布稿件总字数：约 {pub_cn_count} 字")
    if high_overlap_words:
        print(f"\n⚠️  需要关注的意象词汇重叠（{len(high_overlap_words)} 个）：")
        for word, nc, pc in sorted(high_overlap_words, key=lambda x: x[2], reverse=True):
            print(f"   - 「{word}」 — 新稿 {nc} 次 / 已发布稿件共 {pc} 次")
    else:
        print("\n✅ 核心意象词汇无明显重叠。")

if __name__ == '__main__':
    main()
