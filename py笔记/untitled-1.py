#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
笔记搜索工具
功能：在笔记文件中搜索关键词并显示结果
"""

import os


def search_notes(note_file, keyword):
    """
    在笔记文件中搜索关键词
    
    Args:
        note_file: 笔记文件路径
        keyword: 搜索关键词
    
    Returns:
        包含搜索结果的列表，每个元素为(行号, 内容)元组
    """
    results = []
    
    try:
        with open(note_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for i, line in enumerate(lines, 1):  # 行号从1开始
            if keyword in line:
                results.append((i, line.strip()))
                
    except FileNotFoundError:
        print(f"错误：找不到文件 {note_file}")
    except Exception as e:
        print(f"错误：{e}")
    
    return results


def display_results(results, keyword):
    """
    显示搜索结果
    
    Args:
        results: 搜索结果列表
        keyword: 搜索关键词
    """
    if not results:
        print(f"未找到包含 '{keyword}' 的内容")
        return
    
    print(f"找到 {len(results)} 个包含 '{keyword}' 的结果：")
    print("-" * 80)
    
    for line_num, content in results:
        # 高亮显示关键词
        highlighted = content.replace(keyword, f"\033[31m{keyword}\033[0m")
        print(f"第 {line_num} 行: {highlighted}")
    
    print("-" * 80)


if __name__ == "__main__":
    # 笔记文件路径
    note_file = "笔记.py"
    
    # 检查文件是否存在
    if not os.path.exists(note_file):
        print(f"错误：找不到文件 {note_file}")
        print("请确保该脚本与笔记文件在同一目录下，或修改脚本中的文件路径")
    else:
        # 获取用户输入的关键词
        keyword = input("请输入要搜索的关键词：")
        
        if keyword:
            # 执行搜索
            results = search_notes(note_file, keyword)
            # 显示结果
            display_results(results, keyword)
        else:
            print("错误：关键词不能为空")
