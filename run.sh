# run.sh
#!/bin/bash

 python run.py \
 	--preprocess yes \
 	--file unicode_data_files/emoji-sequences.txt \
 	--render_unicode False \
 	--save_path emoji_list/emoji-sequence_v16.py

 python run.py \
 	--preprocess yes \
 	--file unicode_data_files/emoji-zwj-sequences.txt \
 	--render_unicode False \
 	--save_path emoji_list/emoji-zwj-sequence_v16.py
