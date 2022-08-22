set dt=%date%
set tm=%time: =0%
echo %tm%

python .\get_token.py
python .\trade_form.py
