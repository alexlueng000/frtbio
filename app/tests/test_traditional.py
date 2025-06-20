import unittest
from opencc import OpenCC

# 被测试函数
def simplify_to_traditional(text: str) -> str:
    """
    将简体中文转换为繁体中文。
    
    参数：
        text (str): 简体中文字符串。
        
    返回：
        str: 转换后的繁体中文字符串。
    """
    cc = OpenCC('s2t')  # s2t 表示 Simplified to Traditional
    return cc.convert(text)

# 单元测试类
class TestSimplifyToTraditional(unittest.TestCase):
    def test_basic_conversion(self):
        self.assertEqual(simplify_to_traditional("中华人民共和国"), "中華人民共和國")
        self.assertEqual(simplify_to_traditional("汉字"), "漢字")
        self.assertEqual(simplify_to_traditional("电脑"), "電腦")

    def test_empty_string(self):
        self.assertEqual(simplify_to_traditional(""), "")

    def test_non_chinese_characters(self):
        self.assertEqual(simplify_to_traditional("123 ABC !@#"), "123 ABC !@#")

if __name__ == "__main__":
    unittest.main()