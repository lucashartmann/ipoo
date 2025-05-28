import Locomotiva
import Vagao
import Trem

locomotiva1 = Locomotiva.Locomotiva(100.0, 500.0)
locomotiva2 = Locomotiva.Locomotiva(100.0, 500.0)
locomotiva3 = Locomotiva.Locomotiva(100.0, 500.0)

vagao1 = Vagao.Vagao(200.0)
vagao2 = Vagao.Vagao(500.0)
vagao3 = Vagao.Vagao(100.0)

trem1 = Trem.Trem(locomotiva1, vagao1)

print(trem1)

trem1.engatar(vagao2)
trem1.engatar(locomotiva2)
trem1.engatar(vagao3)

print(trem1)

trem1.desengatar(vagao2)

print(trem1)
