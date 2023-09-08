已注销 47370    nohup python -u train.py  --out_model  'parameters_100sumdata_850windows_olddata_50epoch.pt' --epoch 20 --window_size=850 > train_loss.log 2>&1 &
python train.py  --out_model  'parameters_100sumdata_1000windows_olddata_50epoch.pt' --epoch 20 --window_size 1000
12463     nohup python -u train.py  --out_model  'parameters_100sumdata_800windows_olddata_50epoch.pt' --epoch 20 --window_size=800 > train_loss2.log 2>&1 &
34534     nohup python -u train.py  --out_model  'parameters_100sumdata_950windows_olddata_50epoch.pt' --epoch 20 --window_size=950 > train_loss3.log 2>&1 &
29924  nohup python -u train.py  --out_model  'parameters_100sumdata_600windows_olddata_50epoch.pt' --epoch 20 --window_size=600 > train_loss4.log 2>&1 &
47123  nohup python -u train.py  --out_model  'parameters_100sumdata_1000windows_olddata_50epoch.pt' --epoch 20 --window_size=1000 > train_loss5.log 2>&1 &
20767   nohup python -u train.py  --out_model  'parameters_100sumdata_400windows_olddata_50epoch.pt' --epoch 20 --window_size=400 > train_loss6.log 2>&1 &
其实是20

900已经三十个了   35了


12463     nohup python -u train.py  --in_model  'parameters_100sumdata_800windows_olddata_50epoch.pt' --out_model 'parameters_100sumdata_800windows_olddata_50epoch_30percentage.pt' --epoch 10 --window_size=800 > train_loss7.log 2>&1 &
34534     nohup python -u train.py  --in_model  'parameters_100sumdata_950windows_olddata_50epoch.pt' --out_model 'parameters_100sumdata_950windows_olddata_50epoch_30percentage.pt' --epoch 10 --window_size=950 > train_loss8.log 2>&1 &
29924  nohup python -u train.py  --in_model  'parameters_100sumdata_600windows_olddata_50epoch.pt' --out_model 'parameters_100sumdata_600windows_olddata_50epoch_30percentage.pt' --epoch 10 --window_size=600 > train_loss9.log 2>&1 &
20767   nohup python -u train.py  --in_model  'parameters_100sumdata_400windows_olddata_50epoch.pt' --out_model 'parameters_100sumdata_400windows_olddata_50epoch_30percentage.pt'  --epoch 10 --window_size=400 > train_loss10.log 2>&1 &
47123  nohup python -u train.py  --in_model  'parameters_100sumdata_1000windows_olddata_50epoch.pt' --out_model 'parameters_100sumdata_1000windows_olddata_50epoch_30percentage.pt' --epoch 10 --window_size=1000 > train_loss11.log 2>&1 &
七号服务器48100 nohup python -u train.py  --out_model  'parameters_100sumdata_200windows_olddata_50epoch.pt' --epoch 20 --window_size=200 > train_loss12.log 2>&1 &
八号服务器19952 nohup python -u train.py  --out_model  'parameters_100sumdata_1200windows_olddata_50epoch.pt' --epoch 20 --window_size=1200 > train_loss13.log 2>&1 &


20767   nohup python -u train.py  --in_model  'parameters_100sumdata_400windows_olddata_50epoch_30percentage.pt' --out_model 'parameters_100sumdata_400windows_olddata_50epoch_40percentage.pt'  --epoch 10 --window_size=400 > train_loss14.log 2>&1 &
12463     nohup python -u train.py  --in_model  'parameters_100sumdata_800windows_olddata_50epoch_30percentage.pt' --out_model 'parameters_100sumdata_800windows_olddata_50epoch_40percentage.pt' --epoch 10 --window_size=800 > train_loss15.log 2>&1 &
34534     nohup python -u train.py  --in_model  'parameters_100sumdata_950windows_olddata_50epoch_30percentage.pt' --out_model 'parameters_100sumdata_950windows_olddata_50epoch_40percentage.pt' --epoch 10 --window_size=950 > train_loss16.log 2>&1 &
47123  nohup python -u train.py  --in_model  'parameters_100sumdata_1000windows_olddata_50epoch_30percentage.pt' --out_model 'parameters_100sumdata_1000windows_olddata_50epoch_40percentage.pt' --epoch 10 --window_size=1000 > train_loss17.log 2>&1 &



20767   nohup python -u train.py  --in_model  'parameters_100sumdata_400windows_olddata_50epoch_40percentage.pt' --out_model 'parameters_100sumdata_400windows_olddata_50epoch_50percentage.pt'  --epoch 10 --window_size=400 > train_loss18.log 2>&1 &
34534   nohup python -u train.py  --in_model  'parameters_100sumdata_950windows_olddata_50epoch_40percentage.pt' --out_model 'parameters_100sumdata_950windows_olddata_50epoch_50percentage.pt' --epoch 10 --window_size=950 > train_loss19.log 2>&1 &
47123  nohup python -u train.py  --in_model  'parameters_100sumdata_1000windows_olddata_50epoch_40percentage.pt' --out_model 'parameters_100sumdata_1000windows_olddata_50epoch_50percentage.pt' --epoch 10 --window_size=1000 > train_loss20.log 2>&1 &
八号服务器19952 nohup python -u train.py  --in_model  'parameters_100sumdata_1200windows_olddata_50epoch.pt'  --out_model  'parameters_100sumdata_1200windows_olddata_50epoch_30percentage.pt' --epoch 10 --window_size=1200 > train_loss21.log 2>&1 &


八号服务器19952 nohup python -u train.py  --in_model  'parameters_100sumdata_1200windows_olddata_50epoch_30percentage.pt'  --out_model  'parameters_100sumdata_1200windows_olddata_50epoch_40percentage.pt' --epoch 10 --window_size=1200 > train_loss22.log 2>&1 &