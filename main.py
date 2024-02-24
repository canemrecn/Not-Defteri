import tkinter as tk
notes = []
def create_note():
    title = entry_title.get()
    content = entry_content.get("1.0", tk.END)
    note = {"title": title, "content": content}
    notes.append(note)
    lbl_status.config(text="Not oluşturuldu.", fg="green")
    entry_title.delete(0, tk.END)
    entry_content.delete("1.0", tk.END)
def view_notes():
    if not notes:
        lbl_status.config(text="Henüz not bulunmuyor.", fg="red")
        return
    lbl_status.config(text="")
    listbox_notes.delete(0, tk.END)
    for i, note in enumerate(notes):
        listbox_notes.insert(tk.END, note["title"])
def edit_note():
    selection = listbox_notes.curselection()
    if not selection:
        lbl_status.config(text="Düzenlemek için bir not seçin.", fg="red")
        return
    index = selection[0]
    note = notes[index]
    entry_title.delete(0, tk.END)
    entry_title.insert(tk.END, note["title"])
    entry_content.delete("1.0", tk.END)
    entry_content.insert(tk.END, note["content"])
    lbl_status.config(text="Not düzenleme modunda.", fg="blue")
def save_note():
    selection = listbox_notes.curselection()
    if not selection:
        lbl_status.config(text="Kaydetmek için bir not seçin.", fg="red")
        return
    index = selection[0]
    note = notes[index]
    title = entry_title.get()
    content = entry_content.get("1.0", tk.END)
    note["title"] = title
    note["content"] = content
    lbl_status.config(text="Not kaydedildi.", fg="green")
def delete_note():
    selection = listbox_notes.curselection()
    if not selection:
        lbl_status.config(text="Silmek için bir not seçin.", fg="red")
        return
    index = selection[0]
    del notes[index]
    lbl_status.config(text="Not silindi.", fg="green")
def clear_status():
    lbl_status.config(text="")
# Pencere oluşturma
window = tk.Tk()
window.title("Not Defteri")
# Başlık etiketi
lbl_title = tk.Label(window, text="Başlık:")
lbl_title.pack()
# Başlık giriş alanı
entry_title = tk.Entry(window)
entry_title.pack()
# İçerik etiketi
lbl_content = tk.Label(window, text="İçerik:")
lbl_content.pack()
# İçerik metin alanı
entry_content = tk.Text(window, height=5)
entry_content.pack()
# Not oluşturma düğmesi
btn_create = tk.Button(window, text="Not Oluştur", command=create_note)
btn_create.pack()
# Notları görüntüleme düğmesi
btn_view = tk.Button(window, text="Notları Görüntüle", command=view_notes)
btn_view.pack()
# Notları düzenleme düğmesi
btn_edit = tk.Button(window, text="Notu Düzenle", command=edit_note)
btn_edit.pack()
# Notu kaydetme düğmesi
btn_save = tk.Button(window, text="Notu Kaydet", command=save_note)
btn_save.pack()
# Notları silme düğmesi
btn_delete = tk.Button(window, text="Notu Sil", command=delete_note)
btn_delete.pack()
# Notlar listesi
listbox_notes = tk.Listbox(window, width=50)
listbox_notes.pack()
# Durum etiketi
lbl_status = tk.Label(window, text="", fg="red")
lbl_status.pack()
# Durum etiketini temizleme
window.bind("<Button-1>", lambda event: clear_status())
# Pencereyi çalıştırma
window.mainloop()
