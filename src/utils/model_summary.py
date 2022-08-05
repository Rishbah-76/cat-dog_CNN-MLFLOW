import io
import logging

from tensorboard import summary

def log_model_summary(model):
    with io.StringIO() as Stream:
        model.summary(
            print_fn=lambda x: Stream.write(f"{x}\n")
        )
        summary_str=Stream.getvalue()
    return summary_str