for _ in range(int(input())):
    s = input()
    idx = s.find('010') & s.find('101')
    print('Bad' if idx == -1 else 'Good')