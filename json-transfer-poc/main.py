import json;

f=open('input.json');
config=json.load(f);
f.close();

config['data']['aws']['aws_access_key_id_2'] = 'new key';
config['data']['aws']['aws_secret_access_key_2'] = 'new secret';

f=open('output.json','w');
json.dump(config,f);
f.close()
