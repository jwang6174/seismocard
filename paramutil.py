import json
import os


class Params:
  def __init__(self, path):
    self.path = path
    self.data = self.init_json(path)
    self.in_channels = self.data['in_channels']
    self.segment_size = self.data['segment_size']
    self.batch_size = self.data['batch_size']
    self.dir_path = self.data['dir_path']
    self.train_path = os.path.join(self.dir_path, self.data['train_path'])
    self.valid_path = os.path.join(self.dir_path, self.data['valid_path'])
    self.test_path = os.path.join(self.dir_path, self.data['test_path'])
    self.checkpoint_path = os.path.join(self.dir_path, self.data['checkpoint_path'])
    self.losses_fig_path = os.path.join(self.dir_path, self.data['losses_fig_path'])
    self.comparisons_path = os.path.join(self.dir_path, self.data['comparisons_path'])
    self.pred_RHC_path = os.path.join(self.dir_path, self.data['pred_RHC_path'])
    self.alpha = self.data['alpha']
    self.beta1 = self.data['beta1']
    self.beta2 = self.data['beta2']

  def init_json(self, path):
    with open(path, 'r') as f:
      return json.load(f)
