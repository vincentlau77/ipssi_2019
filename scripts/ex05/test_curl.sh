set -e


if [ -z $1 ]; then
	                echo "donnez un nom de site"
			                exit 1
				else
					        set +e

						        if curl -s -I $1 >/dev/null ; then
								                echo "OK"
										        else
												                echo  "FAIL"
														                exit 2
																        fi
																	        set -e
																		        # curl  -I $site

																		fi
																		exit 0
