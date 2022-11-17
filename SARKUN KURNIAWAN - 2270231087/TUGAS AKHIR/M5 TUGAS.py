print('##########################################')

print('-------------SARKUN KURNIAWAN-------------')

print('##########################################')


listpilihan=[]
listjumlahbeli=[]
listharga=[]
listjenis=[]
listtotalbelanja=[]
listketerangan=[]
totalbelanja=0
totalsemua=0

def garis() :
    print('##########################################')

print('>>>>>>> T O K O   P A R A B O T A N <<<<<<')

garis()
n_penjual=input('masukan nama penjual :')
n_pembeli=input('nama pembeli         :')
n_alamat =input('alamat pembeli       :')
n_nomerhp=input('nomer hp pembeli     :')
n_tanggal=input('tanggal pembelian    :')
garis()
print('Alat-Alat Perabotan yang tersedia : ')
print('1. Ember                        ')
print('2. Baskom                       ')
print('3. Gayung                       ')
print('4. Keranjang                    ')
print('5. Panci                        ')
print('6. Centong                      ')
print('7. Gantungan Baju               ')
garis()

a=int(input('Berapa Jumlah Barang yang anda inginkan : '))

for i in range(a):
    print(' Jenis Barang ke- ',i+1)
    pilihan=int(input('pilihan [1/2/3/4/5/6/7] : '))
    listpilihan.append(pilihan)
    jumlahbeli=int(input('jumlah beli : '))
    listjumlahbeli.append(jumlahbeli)

    if(listpilihan[i]==1) :
        listjenis.append('Ember                   ')
        listharga.append(15000)
    elif(listpilihan[i]==2) :
        listjenis.append('Baskom                  ')
        listharga.append(10000)
    elif(listpilihan[i]==3) :
        listjenis.append('Gayung                  ')
        listharga.append(8000)
    elif(listpilihan[i]==4) :
        listjenis.append('Keranjang               ')
        listharga.append(12000)
    elif(listpilihan[i]==5) :
        listjenis.append('Panci                   ')
        listharga.append(20000)
    elif(listpilihan[i]==6) :
        listjenis.append('Centong                 ')
        listharga.append(5000)
    elif(listpilihan[i]==7) :
        listjenis.append('Gantungan Baju          ')
        listharga.append(15000)
    else :
        listpilihan = ('Tidak Ada')

    listtotalbelanja.append(listjumlahbeli[i]*listharga[i])

print('>>>>>>> T O K O   P A R A B O T A N <<<<<<')
print('##########################################')

print('Nama Penjual           : ', n_penjual)
print('Kepada Yth, Bpk/Ibu    : ', n_pembeli)
print('alamat pembeli         : ', n_alamat )
print('nomer hp pembeli       : ', n_nomerhp)

print('##########################################')

print('> > > > > > > > S A L E S < < < < < < < <')

print('##########################################')

print('NO|JENIS|HARGA|JUMLAH BELI|TOTAL BAYAR|ket')

print('------------------------------------------')

for i in range(a):
    totalbelanja=totalbelanja+listjumlahbeli[i]
    totalsemua=totalsemua+listtotalbelanja[i]
    print('------------------------------------------')
print('total belanja            = ', totalbelanja, "(item)")
print('total harga semuanya     = Rp', totalsemua)
print('------------------------------------------')

bayar=int(input('masukan jumlah uang yang di bayar = '))
kembali = bayar - totalsemua
if (totalsemua>=100000) :
    print('uang kembali anda       = Rp. ', kembali)
else :
    print('uang kembali anda       = Rp. ', kembali)

print('------------------------------------------')

print(">>>>TERIMAKASIH SELAMAT DATANG KEMBALI<<<<")
