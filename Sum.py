def two_sum(nums, target):
    # HashMap (Sözlük) oluştur
    hashmap = {}
    
    # Her bir elemanı kontrol et
    for i, num in enumerate(nums):
        # Hedefe ulaşmak için gereken tamamlayıcıyı bul
        complement = target - num
        
        # Eğer tamamlayıcı daha önce görülmüşse
        if complement in hashmap:
            return [hashmap[complement], i]
        
        # Eğer tamamlayıcıyı bulamadıysak, bu numarayı hashmap'e ekle
        hashmap[num] = i
    
    # Eğer hiçbir çözüm bulunamazsa
    return None

# Test Aşaması
nums = [1, 2, 7, 9]  # Test dizisi
target = 9           # Hedef
result = two_sum(nums, target)
print(result)        # Beklenen çıktı: [2, 3] (çünkü 2 + 7 = 9)
