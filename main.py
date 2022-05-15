from matplotlib import pyplot as plt

from fake_random import FakeRandom

data = ['A','B','C','D']
weight = [100,1,1,1]

rd = FakeRandom(data, weight, 100)

re = rd.gets(1000)

times_a = 0
freq_a = []
times_b = 0
freq_b = []
times_c = 0
freq_c = []
times_d = 0
freq_d = []


for i in range(len(re)):
    if re[i]=='A':
        times_a += 1
    freq_a.append(times_a/(i+1))
    if re[i]=='B':
        times_b += 1
    freq_b.append(times_b/(i+1))
    if re[i]=='C':
        times_c += 1
    freq_c.append(times_c/(i+1))
    if re[i]=='D':
        times_d += 1
    freq_d.append(times_d/(i+1))

fig, ax = plt.subplots()

ax.plot(freq_a, label='A')
ax.plot(freq_b, label='B')
ax.plot(freq_c, label='C')
ax.plot(freq_d, label='D')
ax.legend()
plt.show()