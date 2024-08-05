from tqdm import tqdm
from copy import deepcopy
from collections import defaultdict, OrderedDict
import hashlib
from pathlib import Path

from utils.code_error_checker import check_paren_error, check_ast_error
from utils.code_utils import preprocess_unk, code_toks_to_code_string, get_diff_metric, tokenize_python_code
from utils.fairseq_utils import parse_fairseq_preds, fairseq_preprocess, fairseq_generate, fairseq_train