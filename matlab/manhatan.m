load 'dataset.txt'

y(:,1) = dataset(:,2);
y(:,2) = dataset(:,3);
y(:,3) = dataset(:,4);
y(:,4) = dataset(:,5);
y(:,5) = dataset(:,6);
y(:,6) = dataset(:,7);

[n,m] = size(y);

vp = [9 3 6 0 1];

% manhatan
for i = 1 : n
    cont = 0;
    for j = 1 : m
        cont = cont + abs(y(i,j) - vp(1,j));
    end
    R(i,1) = cont;
end


% euclidiana
for i = 1 : f
    cont = 0;
    for j = 1 : c
        cont = cont + (y(i,j) - vp(1,j))^2;
    end
    R(i,1) = sqrt(cont);
end

% busqueda 10 parecidos 

for i = 1 : 10
    [dato1,pos1] = min(R(:,1));
    [dato2,pos2] = mix(R(:,2));
    R(pos1,1) = 100
    R(pos2,2) = 100

    matrix(i,1) = pos1;
    matrix(i,2) = dato1;
    matrix(i,3) = pos2;
    matrix(i,4) = dato2;
end