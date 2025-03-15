
# return을 계속 해주는 이유는 z(2) - z(1)를 호출하면 z(1)에서 값을 호출 스택이 z(1) 값을 z(2)가 받아서 출력

def z(n, tar_r, tar_c, z_count):
    if n == 1: # 2x2박스가 되면
        r = 0
        c = 0
        for dc, dr in direction:
            c += dc
            r += dr
            if r == tar_r and c == tar_c:
                return z_count
            z_count += 1
            
    half_width = 2 ** (n-1)
    dz = int(((2**n)**2 / 4))
    
    # r행 c열일 때 
    # r이l 2^(n-1)보다 작고 c도 2^(n-1)보다 작으면  1사분면
    if tar_c < half_width and tar_r < half_width:
        return z(n-1, tar_r, tar_c, z_count)

    # r이 2^(n-1)보다 작고 c가 2^(n-1)보다 크거나 같으면 2사분면
    if tar_c >= half_width and tar_r < half_width:
        z_count += (dz*1)
        return z(n-1, tar_r, tar_c-half_width, z_count)

    # r이 2^(n-1)보다 크거나 같고 c가 2^(n-1)보다 작으면 3사분면
    if tar_c < half_width and tar_r >= half_width:
        z_count += (dz*2)
        return z(n-1, tar_r-half_width, tar_c, z_count)

    # r이 2^(n-1)보다 크거나 같고 c도 2^(n-1)보다 크거나 같으면 4사분면
    if tar_c >= half_width and tar_r >= half_width:
        z_count += (dz*3)
        return z(n-1, tar_r-half_width, tar_c-half_width, z_count)


n,tar_r,tar_c = map(int, input().split())
z_count = 0
direction = [(0,0), (1,0), (-1,1), (1,0)]
print(z(n, tar_r, tar_c, z_count))