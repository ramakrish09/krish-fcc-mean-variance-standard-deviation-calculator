import numpy as np

def calculate(list):
  calculations = {}
  length = len(list)
  if length < 9:
    raise ValueError('List must contain nine numbers.')
  
  nparr = np.array(list)
  newarr = nparr.reshape(3, 3)
  #print(nparr)
  #print(newarr)
  
  npmean0 = np.mean(newarr, axis=0)
  npmean1 = np.mean(newarr, axis=1)
  npmeanFlT = np.mean(newarr, axis=None)
  
  #print(npmean0.tolist())
  #print(npmean1.tolist())
  #print(npmeanFlT.tolist())

  npmean = []
  npmean.append(npmean0.tolist())
  npmean.append(npmean1.tolist()) 
  npmean.append(npmeanFlT.tolist()) 
  #print(npmean)

  calculations['mean'] = npmean
  #print(calculations)

  npvar0 = np.var(newarr, axis=0)
  npvar1 = np.var(newarr, axis=1)
  npvarFlT = np.var(newarr, axis=None)

  npvar = []
  npvar.append(npvar0.tolist())
  npvar.append(npvar1.tolist()) 
  npvar.append(npvarFlT.tolist())

  calculations['variance'] = npvar
  #print(calculations)

  npstd0 = np.std(newarr, axis=0)
  npstd1 = np.std(newarr, axis=1)
  npstdFlT = np.std(newarr, axis=None)

  npstd = []
  npstd.append(npstd0.tolist())
  npstd.append(npstd1.tolist()) 
  npstd.append(npstdFlT.tolist())

  calculations['standard deviation'] = npstd
  #print(calculations)

  npmax0 = np.max(newarr, axis=0)
  npmax1 = np.max(newarr, axis=1)
  npmaxFlT = np.max(newarr, axis=None)

  npmax = []
  npmax.append(npmax0.tolist())
  npmax.append(npmax1.tolist()) 
  npmax.append(npmaxFlT.tolist())

  calculations['max'] = npmax
  #print(calculations)

  npmin0 = np.min(newarr, axis=0)
  npmin1 = np.min(newarr, axis=1)
  npminFlT = np.min(newarr, axis=None)

  npmin = []
  npmin.append(npmin0.tolist())
  npmin.append(npmin1.tolist()) 
  npmin.append(npminFlT.tolist())

  calculations['min'] = npmin
  #print(calculations)

  npsum0 = np.sum(newarr, axis=0)
  npsum1 = np.sum(newarr, axis=1)
  npsumFlT = np.sum(newarr, axis=None)

  npsum = []
  npsum.append(npsum0.tolist())
  npsum.append(npsum1.tolist()) 
  npsum.append(npsumFlT.tolist())

  calculations['sum'] = npsum

  return calculations