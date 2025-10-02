def tinh_tien(soVeThuong: int, soVe3D: int, tuoi: int):
    if not (0 <= soVeThuong <= 50):
        return "Invalid"
    if not (0 <= soVe3D <= 50):
        return "Invalid"  
    if tuoi <= 0:   # bổ sung kiểm tra tuổi
        return "Invalid"
    
    base = soVeThuong * 70000 + soVe3D * 120000 
    if tuoi <= 22 or tuoi >= 60:
        base *= 0.85      
    return int(round(base))
