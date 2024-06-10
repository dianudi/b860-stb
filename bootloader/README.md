# B860h V1/V2 Bootloader

U-boot bootloader untuk STB B860H V1/V2 untuk booting sistem operasi Armbian atau OpenWRT

### Cara Install

Pastikan STB B860H sudah dalam keadaan di unlock serta di root.
Pastikan juga sdcard sudah di burn sistem operasi Armbian atau Openwrt dan dimasukkan di slot sdcard.

- Install aplikasi Terminal Emulator lalu buka.
- Download file `uboot.bin` simpan di folder download.
- Ketik `su` lalu allow use root.
- Ketik `dd if=/sdcard/Download/uboot.bin of=/dev/block/bootloader`.
- Ketik `reboot update`, STB harusnya tidak akan booting ke Android.
