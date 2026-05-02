
out_dir = 'out-shakespeare-char-layers-7'
eval_interval = 250
eval_iters = 100
log_interval = 50

always_save_checkpoint = True

wandb_log = False
wandb_project = 'shakespeare-char'
wandb_run_name = 'layers-7-heads-4'

dataset = 'shakespeare_char'
gradient_accumulation_steps = 1
batch_size = 64
block_size = 256

n_layer = 7
n_head = 4
n_embd = 128
dropout = 0.2

learning_rate = 1e-3
max_iters = 2000
lr_decay_iters = 2000
min_lr = 1e-4
beta2 = 0.99

warmup_iters = 100

device = 'cuda'
compile = False
