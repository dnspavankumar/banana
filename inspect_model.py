import h5py
import json

with h5py.File('helmet-nonhelmet_cnn.h5', 'r') as f:
    print('Keys:', list(f.keys()))
    if 'model_config' in f.attrs:
        config = json.loads(f.attrs['model_config'])
        print('\nModel Architecture:')
        for i, layer in enumerate(config['config']['layers']):
            print(f"{i+1}. {layer['class_name']}: {layer['config']}")
