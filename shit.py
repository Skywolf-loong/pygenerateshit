import random
import string
from typing import List, Dict, Tuple

class CppShitMountainGenerator:
    def __init__(self):
        self.used_names = set()
        self.current_level = 0
        self.max_level = 5
        self.complexity = 1
        self.functions = []  # 存储生成的函数信息 (name, return_type, params)
        self.global_vars = []  # 存储全局变量信息
        
    def generate_random_name(self, length=10) -> str:
        """生成随机名称，确保不重复"""
        while True:
            name = ''.join(random.choices(string.ascii_letters, k=length))
            if name not in self.used_names:
                self.used_names.add(name)
                return name
    
    def generate_random_type(self) -> str:
        """生成随机类型"""
        types = ["int", "double", "float", "long", "bool", "char"]
        return random.choice(types)
    
    def generate_random_value(self, var_type: str) -> str:
        """根据类型生成随机值"""
        if var_type == "int":
            return str(random.randint(-1000, 1000))
        elif var_type == "double" or var_type == "float":
            return f"{random.uniform(-100.0, 100.0):.2f}f"
        elif var_type == "bool":
            return random.choice(["true", "false"])
        elif var_type == "char":
            return f"'{random.choice(string.ascii_letters)}'"
        elif var_type == "long":
            return f"{random.randint(-10000, 10000)}L"
        return "0"
    
    def generate_constant_definition(self) -> str:
        """生成常量定义"""
        const_type = self.generate_random_type()
        const_name = self.generate_random_name(12)
        const_value = self.generate_random_value(const_type)
        return f"const {const_type} {const_name} = {const_value};"
    
    def generate_global_variable(self) -> str:
        """生成全局变量"""
        var_type = self.generate_random_type()
        var_name = self.generate_random_name(12)
        var_value = self.generate_random_value(var_type)
        self.global_vars.append((var_type, var_name))
        return f"{var_type} {var_name} = {var_value};"
    
    def generate_useless_calculation(self, return_type: str = "void") -> str:
        """生成无效运算"""
        var1 = self.generate_random_name(8)
        var2 = self.generate_random_name(8)
        var3 = self.generate_random_name(8)
        
        operations = ["+", "-", "*", "/", "%"]
        op1 = random.choice(operations)
        op2 = random.choice(operations)
        
        # 对于bool类型，使用条件表达式
        if return_type == "bool":
            return f"""
        {self.generate_random_type()} {var1} = {random.randint(1, 100)};
        {self.generate_random_type()} {var2} = {random.randint(1, 100)};
        bool {var3} = ({var1} {op1} {var2} {op2} {random.randint(1, 100)}) != 0;
        """
        else:
            return f"""
        {self.generate_random_type()} {var1} = {random.randint(1, 100)};
        {self.generate_random_type()} {var2} = {random.randint(1, 100)};
        {self.generate_random_type()} {var3} = {var1} {op1} {var2} {op2} {random.randint(1, 100)};
        """
    
    def generate_useless_api_call(self) -> str:
        """生成无效系统API调用"""
        apis = [
            "Sleep(0);",
            "GetCurrentProcessId();",
            "GetTickCount();",
            "GetLastError();",
            "SYSTEMTIME sysTime; GetSystemTime(&sysTime);",
            "IsDebuggerPresent();"
        ]
        return f"        {random.choice(apis)}"
    
    def generate_useless_output(self) -> str:
        """生成无效控制台输出"""
        messages = [
            "\"Processing data...\"",
            "\"Calculating result...\"", 
            "\"Initializing components...\"",
            "\"Verifying parameters...\"",
            "\"Executing operation...\"",
            "\"Checking status...\""
        ]
        var_name = self.generate_random_name(8)
        return f"""
        std::string {var_name} = {random.choice(messages)};
        std::cout << {var_name} << std::endl;
        """
    
    def generate_function_call(self) -> str:
        """生成函数调用"""
        if not self.functions:
            return ""
        
        func_info = random.choice(self.functions)
        func_name, return_type, params = func_info
        
        # 生成参数
        args = []
        for param_type, param_name in params:
            args.append(self.generate_random_value(param_type))
        
        args_str = ", ".join(args)
        
        if return_type == "void":
            return f"        {func_name}({args_str});"
        else:
            result_var = self.generate_random_name(8)
            return f"""
        {return_type} {result_var} = {func_name}({args_str});
        // Unused result: {result_var}
        """
    
    def generate_for_loop(self, content: str) -> str:
        """生成for循环"""
        loop_var = self.generate_random_name(8)
        comparison = random.choice(["<", "<="])
        end_value = random.randint(5, 20)
        
        return f"""
        for(int {loop_var} = 1; {loop_var} {comparison} {end_value}; {loop_var}++) {{
            {content}
        }}
        """
    
    def generate_return_statement(self, return_type: str) -> str:
        """根据返回类型生成return语句"""
        if return_type == "void":
            return ""
        elif return_type == "int":
            return f"        return {random.randint(0, 100)};"
        elif return_type == "double":
            return f"        return {random.uniform(0.0, 1.0):.2f};"
        elif return_type == "float":
            return f"        return {random.uniform(0.0, 1.0):.2f}f;"
        elif return_type == "bool":
            return f"        return {'true' if random.random() > 0.5 else 'false'};"
        elif return_type == "long":
            return f"        return {random.randint(0, 1000)}L;"
        elif return_type == "char":
            return f"        return '{random.choice(string.ascii_letters)}';"
        else:
            return f"        return {self.generate_random_value(return_type)};"
    
    def generate_function_definition(self, level: int) -> str:
        """生成函数定义"""
        func_name = self.generate_random_name(12)
        return_type = random.choice(["void", "int", "double", "bool"])
        
        # 生成参数
        param_count = random.randint(0, 3)
        params = []
        for i in range(param_count):
            param_type = self.generate_random_type()
            param_name = self.generate_random_name(8)
            params.append((param_type, param_name))
        
        param_str = ", ".join([f"{ptype} {pname}" for ptype, pname in params])
        function_body = self.generate_function_body(level, return_type)
        
        # 存储函数信息
        self.functions.append((func_name, return_type, params))
        
        return f"""
{return_type} {func_name}({param_str}) {{
{function_body}
}}
"""
    
    def generate_function_body(self, level: int, return_type: str) -> str:
        """生成函数体内容"""
        if level >= self.max_level:
            return self.generate_return_statement(return_type)
        
        body_lines = []
        
        # 生成局部变量
        var_count = random.randint(2, 5)
        for _ in range(var_count):
            var_type = self.generate_random_type()
            var_name = self.generate_random_name(8)
            var_value = self.generate_random_value(var_type)
            body_lines.append(f"    {var_type} {var_name} = {var_value};")
        
        # 生成内容块
        content_blocks = random.randint(3, 8)
        for _ in range(content_blocks):
            action = self.choose_action(level)
            body_lines.append(self.execute_action(action, level, return_type))
        
        # 添加return语句（非void函数）
        if return_type != "void":
            body_lines.append(self.generate_return_statement(return_type))
        
        return "\n".join(body_lines)
    
    def choose_action(self, current_level: int) -> str:
        """根据当前层级选择动作"""
        if current_level == 0:
            # 第一层只能生成本层代码或进入下一层
            weights = [0.6, 0.0, 0.3, 0.1]  # 本层, 退出, 下一层, 函数调用
        else:
            weights = [0.5, 0.2, 0.2, 0.1]  # 本层, 退出, 下一层, 函数调用
        
        actions = ["current", "exit", "next", "call"]
        return random.choices(actions, weights=weights)[0]
    
    def execute_action(self, action: str, current_level: int, return_type: str) -> str:
        """执行选择的动作"""
        if action == "current":
            # 生成本层代码
            options = [
                self.generate_useless_calculation(return_type),
                self.generate_useless_api_call(),
                self.generate_useless_output()
            ]
            return random.choice(options)
        
        elif action == "call" and self.functions:
            # 调用已生成的函数
            return self.generate_function_call()
        
        elif action == "next" and current_level < self.max_level - 1:
            # 生成下一层入口
            next_level_content = self.generate_function_body(current_level + 1, return_type)
            return self.generate_for_loop(next_level_content)
        
        else:
            # 退出或无法进入下一层时，生成普通代码
            return self.generate_useless_calculation(return_type)
    
    def generate_code(self, complexity: int = 5) -> str:
        """生成完整的C++代码"""
        self.complexity = max(1, min(complexity, 10))
        self.used_names.clear()
        self.current_level = 0
        self.functions = []
        self.global_vars = []
        
        code_parts = []
        
        # 头文件
        code_parts.append("""
#include <iostream>
#include <windows.h>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <complex>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cwchar>
#include <cwctype>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
#include <assert.h>
#include <ctype.h>
#include <errno.h>
#include <float.h>
#include <limits.h>
#include <locale.h>
#include <math.h>
#include <setjmp.h>
#include <signal.h>
#include <stdarg.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <wchar.h>
#include <wctype.h>

#include <iso646.h>

using namespace std;
""")
        
        # 常量定义
        const_count = random.randint(3, 8)
        code_parts.append("// Constants")
        for _ in range(const_count):
            code_parts.append(self.generate_constant_definition())
        
        # 全局变量
        global_count = random.randint(3, 8)
        code_parts.append("\n// Global variables")
        for _ in range(global_count):
            code_parts.append(self.generate_global_variable())
        
        # 函数声明（前向声明）
        func_count = max(2, self.complexity)
        code_parts.append("\n// Function declarations")
        for i in range(func_count):
            func_name = self.generate_random_name(12)
            return_type = random.choice(["void", "int", "double", "bool"])
            param_count = random.randint(0, 3)
            params = []
            for i in range(param_count):
                param_type = self.generate_random_type()
                param_name = self.generate_random_name(8)
                params.append((param_type, param_name))
            
            param_str = ", ".join([f"{ptype} {pname}" for ptype, pname in params])
            code_parts.append(f"{return_type} {func_name}({param_str});")
            self.functions.append((func_name, return_type, params))
        
        # 函数定义
        code_parts.append("\n// Function definitions")
        for func_name, return_type, params in self.functions:
            param_str = ", ".join([f"{ptype} {pname}" for ptype, pname in params])
            function_body = self.generate_function_body(1, return_type)
            code_parts.append(f"""
{return_type} {func_name}({param_str}) {{
{function_body}
}}""")
        
        # 主函数
        code_parts.append("""
int main() {
    // Initialize random operations
    srand(GetTickCount());
    
    // Execute some meaningless operations
    int counter = 0;
    for(int i = 0; i < 10; i++) {
        counter += i * 2;
    }
    
    std::cout << "Program started" << std::endl;
    
    // Call generated functions
""")
        
        # 在主函数中调用一些生成的函数
        call_count = min(5, len(self.functions))
        called_functions = random.sample(self.functions, call_count)
        for func_name, return_type, params in called_functions:
            # 生成参数
            args = []
            for param_type, param_name in params:
                args.append(self.generate_random_value(param_type))
            
            args_str = ", ".join(args)
            
            if return_type == "void":
                code_parts.append(f"    {func_name}({args_str});")
            else:
                result_var = self.generate_random_name(8)
                code_parts.append(f"    {return_type} {result_var} = {func_name}({args_str});")
        
        code_parts.append("""
    std::cout << "Program finished" << std::endl;
    return 0;
}
""")
        
        return "\n".join(code_parts)


def main():
    generator = CppShitMountainGenerator()
    
    try:
        complexity = int(input("请输入代码复杂程度 (1-10): "))
    except ValueError:
        complexity = 5
    
    print("\n" + "="*50)
    print("生成的屎山C++代码:")
    print("="*50)
    
    code = generator.generate_code(complexity)
    print(code)
    
    # 保存到文件
    filename = "shit_mountain.cpp"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    
    print(f"\n代码已保存到: {filename}")
    print("注意: 此代码仅用于演示目的，不建议在生产环境中使用！")

if __name__ == "__main__":
    main()
