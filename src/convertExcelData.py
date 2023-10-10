import pandas as pd
import json
df = pd.read_excel('/Users/way/mydev/llm/llm-test/data/南疆旅游训练整理2.xlsx')
# how='all'：如果一行（或一列）中的所有元素都是NaN，则删除该行（或该列）
# axis=0参数告诉dropna方法只在行上执行删除操作，因此只有空行会被删除，而空列会保留。
df = df.dropna(how='all', axis=0)
df.rename(columns={'问':'instruction', '详细描述':'input', '答':'output'},inplace=True)
print('df: ', df)
def handle_null(value):
  if pd.isna(value):
      return ''
  return value
df['input'] = df['input'].apply(handle_null)
df.to_json(orient='records',path_or_buf='/Users/way/mydev/llm/LLaMA-Efficient-Tuning/data/cloud-micro-travel-nanjiang.json',force_ascii=False)