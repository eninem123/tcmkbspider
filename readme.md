# http://www.tcmkb.cn 中医药知识服务平台搜索结果爬取
技术栈：
随机useragent
beautifulsoup和xpath
将搜索的多个字段内容保存到csv，并且将相关条目加到队列里面无限递归爬取
但是最后会报内存溢出报错。不知道是不是没用队列和多线程的原因

Traceback (most recent call last):
  File "C:\Users\JKXZ\AppData\Local\conda\conda\envs\ai\lib\site-packages\requests\packages\urllib3\response.py", line 302, in _error_catcher
    yield
  File "C:\Users\JKXZ\AppData\Local\conda\conda\envs\ai\lib\site-packages\requests\packages\urllib3\response.py", line 597, in read_chunked
    chunk = self._handle_chunk(amt)
  File "C:\Users\JKXZ\AppData\Local\conda\conda\envs\ai\lib\site-packages\requests\packages\urllib3\response.py", line 563, in _handle_chunk
    self._fp._safe_read(2)  # Toss the CRLF at the end of the chunk.
  File "C:\Users\JKXZ\AppData\Local\conda\conda\envs\ai\lib\http\client.py", line 609, in _safe_read
    raise IncompleteRead(b''.join(s), amt)
http.client.IncompleteRead: IncompleteRead(0 bytes read, 2 more expected)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\JKXZ\AppData\Local\conda\conda\envs\ai\lib\site-packages\requests\models.py", line 738, in generate
    for chunk in self.raw.stream(chunk_size, decode_content=True):
  File "C:\Users\JKXZ\AppData\Local\conda\conda\envs\ai\lib\site-packages\requests\packages\urllib3\response.py", line 432, in stream
    for line in self.read_chunked(amt, decode_content=decode_content):
  File "C:\Users\JKXZ\AppData\Local\conda\conda\envs\ai\lib\site-packages\requests\packages\urllib3\response.py", line 622, in read_chunked
    self._original_response.close()
  File "C:\Users\JKXZ\AppData\Local\conda\conda\envs\ai\lib\contextlib.py", line 77, in __exit__
    self.gen.throw(type, value, traceback)
  File "C:\Users\JKXZ\AppData\Local\conda\conda\envs\ai\lib\site-packages\requests\packages\urllib3\response.py", line 320, in _error_catcher
    raise ProtocolError('Connection broken: %r' % e, e)
requests.packages.urllib3.exceptions.ProtocolError: ('Connection broken: IncompleteRead(0 bytes read, 2 more expected)', IncompleteRead(0 bytes read, 2 more expected))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/JKXZ/Desktop/code/cnmedicine.py", line 178, in <module>
    mm.run()
  File "C:/Users/JKXZ/Desktop/code/cnmedicine.py", line 165, in run
    self.get_deep_html(url,i)
  File "C:/Users/JKXZ/Desktop/code/cnmedicine.py", line 36, in get_deep_html
    html = requests.get(url, headers=self.headers).content
  File "C:\Users\JKXZ\AppData\Local\conda\conda\envs\ai\lib\site-packages\requests\api.py", line 72, in get
    return request('get', url, params=params, **kwargs)
  File "C:\Users\JKXZ\AppData\Local\conda\conda\envs\ai\lib\site-packages\requests\api.py", line 58, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\JKXZ\AppData\Local\conda\conda\envs\ai\lib\site-packages\requests\sessions.py", line 518, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\JKXZ\AppData\Local\conda\conda\envs\ai\lib\site-packages\requests\sessions.py", line 672, in send
    r.content
  File "C:\Users\JKXZ\AppData\Local\conda\conda\envs\ai\lib\site-packages\requests\models.py", line 816, in content
    self._content = bytes().join(self.iter_content(CONTENT_CHUNK_SIZE)) or bytes()
  File "C:\Users\JKXZ\AppData\Local\conda\conda\envs\ai\lib\site-packages\requests\models.py", line 741, in generate
    raise ChunkedEncodingError(e)
requests.exceptions.ChunkedEncodingError: ('Connection broken: IncompleteRead(0 bytes read, 2 more expected)', IncompleteRead(0 bytes read, 2 more expected))

Process finished with exit code 1
