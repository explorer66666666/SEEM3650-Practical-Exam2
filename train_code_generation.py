out_dir = 'out-code-generation'
eval_interval = 250
eval_iters = 100
log_interval = 50

always_save_checkpoint = True

wandb_log = False
wandb_project = 'code-generation'
wandb_run_name = 'babygpt-python-code'

dataset = 'code_generation'
gradient_accumulation_steps = 1
batch_size = 64
block_size = 256

n_layer = 4
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
