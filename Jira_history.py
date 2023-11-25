
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav



  File "toxic.py", line 12, in <module>
    toxic_sum = pipe([row['text_client']])
  File "C:\Program Files\Python38\lib\site-packages\transformers\pipelines\text_classification.py", line 156, in __call__
    result = super().__call__(*args, **kwargs)
  File "C:\Program Files\Python38\lib\site-packages\transformers\pipelines\base.py", line 1121, in __call__
    outputs = list(final_iterator)
  File "C:\Program Files\Python38\lib\site-packages\transformers\pipelines\pt_utils.py", line 124, in __next__
    item = next(self.iterator)
  File "C:\Program Files\Python38\lib\site-packages\transformers\pipelines\pt_utils.py", line 125, in __next__
    processed = self.infer(item, **self.params)
  File "C:\Program Files\Python38\lib\site-packages\transformers\pipelines\base.py", line 1046, in forward
    model_outputs = self._forward(model_inputs, **forward_params)
  File "C:\Program Files\Python38\lib\site-packages\transformers\pipelines\text_classification.py", line 187, in _forward
    return self.model(**model_inputs)
  File "C:\Program Files\Python38\lib\site-packages\torch\nn\modules\module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "C:\Program Files\Python38\lib\site-packages\torch\nn\modules\module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "C:\Program Files\Python38\lib\site-packages\transformers\models\bert\modeling_bert.py", line 1564, in forward
    outputs = self.bert(
  File "C:\Program Files\Python38\lib\site-packages\torch\nn\modules\module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "C:\Program Files\Python38\lib\site-packages\torch\nn\modules\module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "C:\Program Files\Python38\lib\site-packages\transformers\models\bert\modeling_bert.py", line 1015, in forward
    embedding_output = self.embeddings(
  File "C:\Program Files\Python38\lib\site-packages\torch\nn\modules\module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "C:\Program Files\Python38\lib\site-packages\torch\nn\modules\module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "C:\Program Files\Python38\lib\site-packages\transformers\models\bert\modeling_bert.py", line 238, in forward
    embeddings += position_embeddings
RuntimeError: The size of tensor a (1681) must match the size of tensor b (512) at non-singleton dimension 1
