from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

import torch


model = AutoModelForSeq2SeqLM.from_pretrained('giliit/capstone_v2')
tokenizer = AutoTokenizer.from_pretrained("giliit/capstone_tokenizer")


def generate(text):
    processed = {}
    inp = f'{text}'
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tokenizer_input = tokenizer(
        inp,
        padding="max_length",
        max_length=256,
        truncation=True,
        return_tensors='pt'
    )

    # 모델과 데이터를 GPU로 이동
    processed["input_ids"] = tokenizer_input["input_ids"].to(device)
    processed["attention_mask"] = tokenizer_input["attention_mask"].to(device)
    model.to(device)

    # 모델 실행
    summary_tokens = model.generate(
            processed["input_ids"],
            attention_mask=processed["attention_mask"],
            decoder_start_token_id=tokenizer.bos_token_id,
            max_length=256,
            pad_token_id=tokenizer.pad_token_id,
            bos_token_id=tokenizer.bos_token_id,
            eos_token_id=tokenizer.eos_token_id
        )

    # 출력 처리
    output = summary_tokens.cpu().detach().tolist()
    text = tokenizer.decode(output[0], skip_special_tokens=True)
    #text = filtering_text(text)
    return text