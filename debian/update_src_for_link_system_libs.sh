#!/bin/sh

echo "Updating Mono.Data.Sqlite.dll references"
find . \( -name "*.am" -or -name "*.in" \) -exec perl -pe 's!-r\:\$\(top_(src|build)dir\)/contrib/Sqlite/Mono\.Data\.Sqlite\.dll!-r:Mono.Data.Sqlite.dll!g' -i {} \;

echo "Updating MySql.Data.dll references"
find . \( -name "*.am" -or -name "*.in" \) -exec perl -pe 's!-r\:\$\(top_(src|build)dir\)/contrib/MySql/MySql\.Data\.dll!\$(shell pkg-config --libs mysql-connector-net)!g' -i {} \;

echo "Deleting reject files (*.rej)"
find -name "*.rej" -delete
