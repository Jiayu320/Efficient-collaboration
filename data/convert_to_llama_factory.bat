@echo off
echo 开始转换处理好的数据为LLaMA-Factory格式...

:: 设置环境变量
set INPUT_DIR=..\dataset\processed\limo
set OUTPUT_DIR=..\dataset\dataset\limo_factory
set OUTPUT_FILE=%OUTPUT_DIR%\llama_factory_data.json

:: 创建输出目录
if not exist %OUTPUT_DIR% mkdir %OUTPUT_DIR%

:: 执行转换
python llama_factory.py --input_dir %INPUT_DIR% --output_file %OUTPUT_FILE% --format llama

echo 转换完成！输出文件: %OUTPUT_FILE%
pause
