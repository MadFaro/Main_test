TologonovAB\Desktop\nemo_model\stt_ru_conformer_ctc_large.nemo.
Transcribing:   0%|                                                                              | 0/1 [00:01<?, ?it/s]
Traceback (most recent call last):
  File "Nemo.py", line 4, in <module>
    transcriptions = quartznet.transcribe(paths2audio_files=wave_file)
  File "C:\Python38\lib\site-packages\torch\utils\_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "C:\Python38\lib\site-packages\nemo\collections\asr\models\ctc_models.py", line 197, in transcribe
    for test_batch in tqdm(temporary_datalayer, desc="Transcribing", disable=not verbose):
  File "C:\Python38\lib\site-packages\tqdm\std.py", line 1178, in __iter__
    for obj in iterable:
  File "C:\Python38\lib\site-packages\torch\utils\data\dataloader.py", line 633, in __next__
    data = self._next_data()
  File "C:\Python38\lib\site-packages\torch\utils\data\dataloader.py", line 677, in _next_data
    data = self._dataset_fetcher.fetch(index)  # may raise StopIteration
  File "C:\Python38\lib\site-packages\torch\utils\data\_utils\fetch.py", line 54, in fetch
    return self.collate_fn(data)
  File "C:\Python38\lib\site-packages\nemo\core\classes\common.py", line 1089, in __call__
    instance._attach_and_validate_output_types(
  File "C:\Python38\lib\site-packages\nemo\core\classes\common.py", line 353, in _attach_and_validate_output_types
    self.__attach_neural_type(res, metadata, depth=0, name=out_types_list[ind][0])
  File "C:\Python38\lib\site-packages\nemo\core\classes\common.py", line 441, in __attach_neural_type
    raise TypeError(
TypeError: Output shape mismatch occured for audio_signal in module AudioToBPEDataset :
Output shape expected = (batch, time) |
Output shape found : torch.Size([1, 3152160, 2])
