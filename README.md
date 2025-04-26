## (ACO) Algoritması Kullanarak Rota İyileştirmesi

Bu proje, teslimat ve lojistik sektöründe kullanılabilecek bir **Karınca Kolonisi Optimizasyonu (ACO) algoritması** ile rotaların iyileştirilmesini hedeflemektedir. Algoritma, şehirler veya dağıtım noktaları arasındaki en kısa ve en verimli yolları bulmak için Karınca Kolonisi Optimizasyonu (ACO) metodunu kullanır.

## Amaç

Projenin amacı, teslimatların en hızlı ve en verimli şekilde yapılabilmesi için araçların ve teslimat noktalarının rotalarını optimize etmektir. Bu algoritma, lojistik ve teslimat sektörlerinde kullanılan **rota planlaması** gibi süreçleri iyileştirmeyi sağlar.

## Temel Fikir

- **Karınca Kolonisi Optimizasyonu (ACO) Algoritması**: ACO, doğada karıncaların, feromonlar bırakarak en kısa yolları bulma davranışlarından ilham alır. Karıncalar, zamanla daha iyi rotalar keşfeder ve bu süreç, algoritma tarafından simüle edilir.
- Algoritma, **birkaç karınca** ile rotaları keşfeder ve her geçen iterasyonda en iyi rotalar üzerinde daha fazla feromon bırakır.
- **Amaç**: Teslimat noktaları arasında en kısa ve en uygun rotaları bularak teslimat süresini ve maliyetini düşürmek.


## Ana Parametreler

- **Alpha (α)**: Feromonların yoldaki etkisi. Değer ne kadar büyükse, o kadar fazla feromon bırakan yollar tercih edilir.
- **Beta (β)**: Yoldaki mesafenin (veya zamanın) etkisi. Değer ne kadar büyükse, daha kısa (veya hızlı) yollar tercih edilir.
- **Rho (ρ)**: Feromon buharlaşma faktörü. Bu parametre, her iterasyonda feromonların ne kadar buharlaşacağını belirler.
- **Q**: Feromon sabiti, karıncalar bir yolu geçtikten sonra feromon bırakma miktarını kontrol eder.
- **Karınca Sayısı**: Her iterasyonda yolları araştıracak olan karınca (veya teslimat) sayısı.
- **Şehir Sayısı**: Teslim edilmesi gereken yerlerin sayısı.


