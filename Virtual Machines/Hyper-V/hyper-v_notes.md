# Hyper-V

Hyper-V specifically provides hardware virtualization.

## Guide
- https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/

## Steps to give internet access
1. Create a new external switch using Virtual Switch Manager and assign to the VM

## Hyper-V setup Pre-requisites

- enable VT in BIOS
- enable all Hyper-V windows features

## Shortcut

```C:\Windows\System32\vmconnect.exe localhost "<nameofvm>"```

## VHD location

```C:\Users\Public\Documents\Hyper-V\Virtual hard disks```

## Devloper Images
- https://developer.microsoft.com/en-us/windows/downloads/virtual-machines


## Common Issues

- fail to add v-switch: https://support.microsoft.com/en-us/help/3101106/you-cannot-create-a-hyper-v-virtual-switch-on-64-bit-versions-of-windo
- Screen blank: https://serverfault.com/questions/220437/remote-desktop-connection-screen-is-totally-black-but-server-is-working-perfectl
- unable to remote into Ubuntu - Disabling Enhanced Session Mode in the Hyper-V settings screen worked perfectly for me.

to try:
ps commands
get-netadaptervmq
set-netadaptervmq -name nicname -enabled $false
