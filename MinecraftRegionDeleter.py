#X:\MinecraftServers\2014 11 29 Matt\world\region
import time, datetime;
import tkinter as tk;
import tkinter.messagebox as tkm;
import tkinter.filedialog as tkf;
import os, sys, shutil;


py_file_location = os.path.dirname(os.path.abspath(__file__));
last_used_path_file_path = os.path.join(py_file_location,"last_used_path.txt");


if(os.path.exists(last_used_path_file_path)):
	last_used_path_file = open(last_used_path_file_path,"r");
	last_used_path = last_used_path_file.read();
	last_used_path_file.close();
else:
	last_used_path = "";



class RegionFile:
	def __init__(self,x,y,size):
		self.x = x;
		self.y = y;
		self.size = size
		self.checked = tk.IntVar();
		self.checked.set(0);
	
	def getFileName(self):
		return str("r."+str(self.x)+"."+str(self.y)+".mca");





root = tk.Tk()
root.title("Minecraft Region Deleter");
root.geometry("+1930+10");

OuterFrame = tk.Frame(root,
	padx=10,
	pady=10
)
OuterFrame.pack(
	fill=tk.BOTH,
	expand=1
);

InnerFrame = tk.Frame(
	OuterFrame,
	padx=10,
	pady=10,
	borderwidth =3,
	relief=tk.SUNKEN
);
InnerFrame.pack(
	fill=tk.BOTH,
	expand=1
);

BottomFrame = tk.Frame(
	OuterFrame,
	padx=10,
	pady=10,
	borderwidth =3,
	relief=tk.SUNKEN
);
BottomFrame.pack(
	fill=tk.X,
	expand=10
);



def update_file_size():
	#a checkbox was clicked... re-tally the world size
	total = 0;
	total_checked = 0;
	for item in fs:
		if item.checked.get()==1:
			total_checked += item.size;
		total += item.size;
	
	Label.configure(
		text = "Size: {:.1f}mb, Selected: {:.1f}mb".format(total/1024/1024,total_checked/1024/1024)
	)
		
			

def Delete_command():
	global indir;
	count = 0;
	for item in fs:
		if item.checked.get()==1:
			count+=1;
			
	if tkm.askyesno("Delete", "Are you sure you want to delete these {} region files?".format(count)):
		if tkm.askyesno("CANNOT BE UNDONE!!", "THIS CANNOT BE UNDONE! FILES GO STRAIGHT TO THE VOID >>> WILL NOT BE IN YOUR TRASHCAN.\nPlease make sure they are backed up.\n\nContinue?"):
			for item in fs:
				if item.checked.get()==1:
					os.unlink(os.path.join(indir,item.getFileName()));
			tkm.showinfo("Deleted", "The selected files were deleted. This program will now terminate.\n\nHope that went well for you :)");
			exit();
				
			

def Backup_command():
	global indir;
	today = datetime.datetime.now();
	#,*today.time
	foldername = "{:04} {:02} {:02} {:02}{:02}{:02} Backup".format(
		today.year,
		today.month,
		today.day,
		today.hour,
		today.minute,
		today.second
	)
	backupdir = os.path.join(indir,foldername);
	if(not os.path.exists(backupdir)):
		os.mkdir(backupdir);
		print("Created backup directory "+backupdir);
	for item in fs:
		if item.checked.get()==1:
			shutil.copy(
				os.path.join(indir,item.getFileName()),
				backupdir
			);
	tkm.showinfo("Region Backup", "Region files backed up in the following folder: \n {}\n\nRemember to clear out these folders later :)".format(backupdir))
			
# BACKUP BUTTON
BackUpBut = tk.Button(
	BottomFrame,
	text = "Backup",
	command=Backup_command,
	fg="green"
);
BackUpBut.grid(
	column=0,
	row=0,
	padx=5
);


# DELETE BUTTON
DeleteBut = tk.Button(
	BottomFrame,
	text = "DELETE",
	command=Delete_command,
	fg="darkred"
);
DeleteBut.grid(
	column=2,
	row=0,
	padx=5
);

# INFO LABLE
Label = tk.Label(BottomFrame);
Label.grid(
	column=1,
	row=0,
	padx=5
)



fs = [];

#lunkz = tkf.askdirectory();
#print(lunkz);
if(os.path.exists(last_used_path)):
	indir = tkf.askdirectory(initialdir=last_used_path,title="Select ../world/region folder");
else:
	indir = tkf.askdirectory();
if(os.path.exists(indir)):
	last_used_path_file = open(os.path.join(py_file_location,"last_used_path.txt"),"w");
	last_used_path_file.write(indir);
else:
	print("no such directory");

for file_root, dirs, filenames in os.walk(indir):
	for f in filenames:
		coord = f.split(".");
		nreg = RegionFile(
			x=int(coord[1]),
			y=int(coord[2]),
			size=os.path.getsize(os.path.join(indir,f))
		)
		fs.append(nreg);
	break;

#  , text="x",x=item[0]*30,y=item[1]*30
Infinity = sys.maxsize;
xl=Infinity;
xg=-Infinity;
yl=Infinity;
yg=-Infinity;
size_g = 0;

print(fs[0].getFileName())

for item in fs:
	if(item.x>xg):
		xg=item.x
		
	if(item.x<xl):
		xl=item.x
		
	if(item.y>yg):
		yg=item.y
		
	if(item.y<yl):
		yl=item.y
		
	if(item.size>size_g):
		size_g = item.size;

for item in fs:
	text_lable = "{0:.2f}mb".format(item.size/1024/1024)+"\n"+item.getFileName();
	w = tk.Checkbutton(
		InnerFrame,
		text=text_lable,
		justify=tk.LEFT,
		variable=item.checked,
		command=update_file_size
	);
	w.region = item;
	w.grid(
		column=(item.x-xl),
		row=(item.y-yl),
		sticky=tk.N+tk.W
	);
update_file_size()
for i in range(0,100):
	InnerFrame.columnconfigure(i, weight=1)
	BottomFrame.columnconfigure(i, weight=1)
for i in range(0,100):
	InnerFrame.rowconfigure(i, weight=1)
	BottomFrame.rowconfigure(i, weight=1)


root.mainloop();
#os.system("pause");