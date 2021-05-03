from my_lrucache import LRUCacheDict

import time
import functools

# Create your tests here.

CACHE = {}


# def query(sql):
#     """被动缓存，也就是当有请求处理完之后才会缓存数据，即第一次请求还需要去实际执行"""
#     try:
#         result = CACHE[sql]
#     except KeyError:
#         time.sleep(1)
#         result = 'execute %s' % sql
#         CACHE[sql] = result
#     return result

# def query(sql):
#     """主动缓存，
#     其一是系统启动时，会自动把所有接口刷一遍，这样用户在访问时缓存就已经存在；
#     其二就是在数据写入时同步更新或写人缓存"""
#
#     result = CACHE.get(sql)
#     if not result:
#         time.sleep(1)
#         result = 'execute %s' % sql
#         CACHE[sql] = result
#     return result

def cache_it(max_size=1024, expiration=60):
    """缓存的装饰器函数"""
    # functools.wraps 的作用 为了保留 函数的签名（ 可以理为保留原函数的所有属 )
    CACHE = LRUCacheDict(max_size=max_size, expiration=expiration)

    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            # repr 的作用是把传递给它的对象都转为字符串
            key = repr(*args, **kwargs)
            try:
                result = CACHE[key]
            except KeyError:
                result = func(*args, **kwargs)
                CACHE[key] = result
            return result

        return inner

    return wrapper


@cache_it(max_size=10, expiration=3)
def query(sql):
    """直接执行，不加缓存"""
    time.sleep(1)
    result = 'execute %s' % sql
    return result


if __name__ == "__main__":
    start = time.time()
    query('SELECT * FROM blog_post')
    print(time.time() - start)

    start = time.time()
    query('SELECT * FROM blog_post')
    print(time.time() - start)
