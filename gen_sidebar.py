import os
from shutil import copyfile
import codecs
import re
from urllib.parse import quote

suffix = ".md"
gen_file_name = "summary.md"
doc_path = "docs"
read_me_file = "README.md"

ignore_files = [gen_file_name, ".git", read_me_file, "images"]


def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)


def print_file(c_dir, depth, sidebar_file, readme_file):
    for f in sorted_alphanumeric(os.listdir(c_dir)):
        re_f = os.path.join(c_dir, f)
        is_d = os.path.isdir(re_f)
        if is_d and f not in ignore_files:
            content = "\t" * depth + "- " + f + "\n"
            sidebar_file.write(content)
            readme_file.write(content)
            print_file(re_f, depth + 1, sidebar_file, readme_file)
        else:
            if suffix in f and f not in ignore_files:
                f_n = os.path.splitext(f)[0]
                content = "\t" * depth + "- [" + f_n + "](/" + quote(re_f[2:]) + ")\n"
                sidebar_file.write(content)
                readme_file.write(content)


def read_tag():
    doc_suffix = "md"
    ignore_dirs = ["./images"]
    tag_head = "## Tag"
    tag_prefix = "- "

    result = {}
    for p_dir, dirs, files in os.walk("./"):
        # p_dir目录，dirs目录下文件夹名列表，files目录下文件名列表
        if p_dir in ignore_dirs:
            continue
        for file in files:
            if doc_suffix not in file:
                continue
            f_p = p_dir + "/" + file
            f = open(f_p)
            line = f.readline()
            while line:
                if line.strip() == tag_head.strip():
                    line = f.readline()
                    while line.startswith(tag_prefix):
                        tag = line[2:].strip()
                        if tag not in result:
                            result[tag] = []
                        result[tag].append((f_p, file[:-3]))
                        line = f.readline()
                    break
                line = f.readline()
            f.close()
    return result


os.chdir(doc_path)
copyfile("../" + read_me_file, read_me_file)

# 为README.md生成目录；生成左侧sidebar(summary.md)
g_f = codecs.open(gen_file_name, 'w', encoding='utf-8')
r_f = codecs.open(read_me_file, 'a', encoding='utf-8')

r_f.write("\n## 标签\n")
tags = read_tag()
for tag in tags:
    r_f.write(f"\n### {tag}\n")
    for file in tags[tag]:
        r_f.write("- [" + file[1] + "](" + file[0] + ")\n")

r_f.write("\n## 目录\n")
print_file(".", 0, g_f, r_f)
g_f.close()
r_f.close()
