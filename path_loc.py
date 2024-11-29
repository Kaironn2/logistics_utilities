from pathlib import Path

mgt_path = Path(__file__).resolve()

mgt_dir = mgt_path.parent

parent_dir = mgt_dir.parent

print(
    f'1 - {mgt_path}',
    f'2 - {mgt_dir}',
    f'3 - {parent_dir}'
)