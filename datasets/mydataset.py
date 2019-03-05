from datasets import fsns

DEFAULT_DATASET_DIR = 'datasets/mydataset'

DEFAULT_CONFIG = {
    'name':
        'MYDATASET',
    'splits': {
        'train': {
            'size': 1,
            'pattern': 'tfexample_train*'
        },
        'test': {
            'size': 1,
            'pattern': 'tfexample_test*'
        }
    },
    'charset_filename':
        'dic.txt',
    'image_shape': (100, 200, 3),
    'num_of_views':
        1,
    'max_sequence_length':
        37,
    'null_code':
        5642,
    'items_to_descriptions': {
        'image':
            'A [100 x 200 x 3] color image.',
        'label':
            'Characters codes.',
        'text':
            'A unicode string.',
        'length':
            'A length of the encoded text.',
        'num_of_views':
            'A number of different views stored within the image.'
    }
}


def get_split(split_name, dataset_dir=None, config=None):
  if not dataset_dir:
    dataset_dir = DEFAULT_DATASET_DIR
  if not config:
    config = DEFAULT_CONFIG

  return fsns.get_split(split_name, dataset_dir, config)
